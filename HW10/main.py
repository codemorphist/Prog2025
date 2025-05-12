import sqlite3


conn = None
cursor = None


def init_db():
    global conn, cursor

    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dish_id INTEGER,
        description TEXT,
        FOREIGN KEY (dish_id) REFERENCES dishes(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipe_ingredients (
        recipe_id INTEGER,
        ingredient_id INTEGER,
        quantity TEXT,
        FOREIGN KEY (recipe_id) REFERENCES recipes(id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id)
    )
    ''')
    
    conn.commit()


def add_ingredient(name):
    try:
        cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (name,))
        conn.commit()
        print(f"[+] Ingredient '{name}' was added.")
    except sqlite3.IntegrityError:
        print(f"[!] Ingridient '{name}' already exists.")


def add_dish(name):
    try:
        cursor.execute("INSERT INTO dishes (name) VALUES (?)", (name,))
        conn.commit()
        print(f"[+] Dish '{name}' was added.")
    except sqlite3.IntegrityError:
        print(f"[!] Dish '{name}' already exists.")


def add_recipe(dish_name, description, ingredients_list):
    cursor.execute("SELECT id FROM dishes WHERE name = ?", (dish_name,))
    dish = cursor.fetchone()
    if not dish:
        print(f"[x] Dish '{dish_name}' not found.")
        return

    dish_id = dish[0]
    cursor.execute("INSERT INTO recipes (dish_id, description) VALUES (?, ?)", (dish_id, description))
    recipe_id = cursor.lastrowid

    for ingredient_name, quantity in ingredients_list:
        cursor.execute("SELECT id FROM ingredients WHERE name = ?", (ingredient_name,))
        result = cursor.fetchone()
        if not result:
            print(f"[x] Ingridient '{ingredient_name}' not found.")
            continue
        ingredient_id = result[0]
        cursor.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)",
                       (recipe_id, ingredient_id, quantity))

    conn.commit()
    print(f"[+] Recipe for '{dish_name}' was added.")


def search_recipes(dish_name):
    cursor.execute('''
        SELECT recipes.id, recipes.description 
        FROM recipes
        JOIN dishes ON recipes.dish_id = dishes.id
        WHERE dishes.name = ?
    ''', (dish_name,))
    recipes = cursor.fetchall()
    if not recipes:
        print(f"[?] Recipe for '{dish_name}' not found.")
        return

    for recipe_id, description in recipes:
        print(f"\nRecipe #{recipe_id}: {description}")
        cursor.execute('''
            SELECT ingredients.name, recipe_ingredients.quantity
            FROM recipe_ingredients
            JOIN ingredients ON recipe_ingredients.ingredient_id = ingredients.id
            WHERE recipe_ingredients.recipe_id = ?
        ''', (recipe_id,))
        ingredients = cursor.fetchall()
        for name, quantity in ingredients:
            print(f"- {name}: {quantity}")
        print()


if __name__ == "__main__":
    init_db()
    add_ingredient("Цибуля")
    add_ingredient("Морква")
    add_ingredient("Картопля")

    add_dish("Борщ")

    add_recipe("Борщ", "Варити овочі, додати спеції.",
               [("Цибуля", "100 г"), ("Морква", "150 г"), ("Картопля", "200 г")])

    search_recipes("Борщ")
    search_recipes("Галушки")

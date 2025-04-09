import os
import json

from app.settings import DB_PATH


DB = None


def create_empty():
    with open(DB_PATH, "w") as f:
        json.dump({"toys": []}, f)


def load():
    global DB

    if not os.path.exists(DB_PATH):
        create_empty()

    with open(DB_PATH, "r") as f:
        DB = json.load(f)


def db_is_loaded():
    if DB is None:
        raise Exception("DB not loaded")


def save():
    db_is_loaded()
    with open(DB_PATH, "w") as f:
        f.write(json.dumps(DB,indent=4))


def close():
    global DB
    db_is_loaded()
    DB = None


def safe_close():
    db_is_loaded()
    save()
    close()


def insert(obj):
    db_is_loaded()
    DB["toys"].append(obj)
    save()


def insert_toy(name: str, price: float, age_range: tuple[int, int]):
    db_is_loaded()
    toy = {
        "name": name,
        "price": float(f"{price:.2f}"),
        "age_range": age_range,
    }
    insert(toy)


def delete_toy(id: int) -> dict:
    db_is_loaded()
    toy = DB["toys"].pop(id)
    save()
    return toy 


def get_toys() -> list[dict]:
    db_is_loaded()
    return DB["toys"]


# Load DB when module using
load()

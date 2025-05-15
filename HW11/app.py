from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

class Person:
    def __init__(self, name, byear):
        self.name = name
        self.byear = byear
        

class RoomType:
    def __init__(self, id, name, rate):
        self.id = id
        self.name = name
        self.rate = rate



class Guest(Person):
    def __init__(self, name, byear, room_type_id, nights):
        super().__init__(name, byear)
        self.room_type_id = room_type_id
        self.nights = nights

    def calculate_total(self, rate):
        return self.nights * rate


room_types = [
    ('Одномісний', 500),
    ('Двомісний', 800),
    ('Люкс', 1500)
] 


def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS room_types (
                id INTEGER PRIMARY KEY,
                name TEXT,
                rate REAL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS guests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                byear TEXT,
                room_type_id INTEGER,
                nights INTEGER,
                FOREIGN KEY(room_type_id) REFERENCES room_types(id)
            )
        ''')
        c.execute('SELECT COUNT(*) FROM room_types')
        if c.fetchone()[0] == 0:
            c.executemany('INSERT INTO room_types (name, rate) VALUES (?, ?)', room_types)
        conn.commit()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM room_types')
    rooms = c.fetchall()
    
    if request.method == 'POST':
        name = request.form['name']
        byear = request.form['byear']
        room_type_id = int(request.form['room_type_id'])
        nights = int(request.form['nights'])

        guest = Guest(name, byear, room_type_id, nights)

        c.execute('INSERT INTO guests (name, byear, room_type_id, nights) VALUES (?, ?, ?, ?)',
                  (guest.name, guest.byear, guest.room_type_id, guest.nights))
        conn.commit()
        return redirect('/guests')
    
    return render_template('register.html', rooms=rooms)


@app.route('/guests')
def guests():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        SELECT g.name, g.byear, r.name, r.rate, g.nights 
        FROM guests g
        JOIN room_types r ON g.room_type_id = r.id
    ''')
    data = c.fetchall()
    guests = []
    for name, byear, room_name, rate, nights in data:
        person = Guest(name, byear, None, nights)
        guests.append({
            'name': name,
            'byear': byear,
            'room': room_name,
            'rate': rate,
            'nights': nights,
            'total': person.calculate_total(rate)
        })
    return render_template('guests.html', guests=guests)


if __name__ == '__main__':
    init_db()
    app.run(port=8000)


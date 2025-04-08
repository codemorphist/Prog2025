import os
import json

from app.settings import DB_PATH


DB = None


def create_empty():
    with open(DB_PATH, "w") as f:
        json.dump({"toys": []}, f)


def load():
    global DB

    if DB is not None:
        return 

    if not os.path.exists(DB_PATH):
        create_empty()

    with open(DB_PATH, "r") as f:
        DB = json.load(f)


def save():
    with open(DB_PATH, "w") as f:
        f.write(json.dumps(DB,indent=4))


def close():
    global DB
    DB = None


def safe_close():
    save()
    close()


def insert(obj):
    if DB is None:
        raise ValueError("Open DB before use it")
    DB["toys"].append(obj)
    save()


def insert_toy(name: str, price: float, age_range: tuple[int, int]):
    toy = {
        "name": name,
        "price": float(f"{price:.2f}"),
        "age_range": age_range,
    }
    insert(toy)


def delete_toy(id: int) -> dict:
    if DB is None:
        raise Exception("DB not loaded")
    return DB["toys"].pop(id)


def get_toys() -> list[dict]:
    return DB["toys"] if DB is not None else []


# Load DB when module using
load()

import os
import json

from app.settings import DB_PATH


DB = None


def create_empty():
    with open(DB_PATH, "w") as f:
        json.dump({}, f)


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
        f.write(json.dumps(DB, indent=4))


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
    save()


# Load DB when module using
load()

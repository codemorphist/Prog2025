import os
import json
from datetime import datetime, timedelta

from app.settings import DB_PATH
from app.models import SUBJECTS

from copy import deepcopy


DB = None


def create_empty():
    with open(DB_PATH, "w") as f:
        db = {
            "subjects": SUBJECTS,
            "students": [],
        }
        json.dump(db, f)


def load():
    global DB

    if not os.path.exists(DB_PATH):
        create_empty()

    with open(DB_PATH, "r") as f:
        DB = json.load(f)

    save()


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


def get_subjects():
    db_is_loaded()
    return DB["subjects"]


def student(name: str, byear: datetime, ayear: datetime, 
            grades: list[int]) -> dict:
    study3y9m = timedelta(days=365*3 + 9*30)

    date_format = "%Y-%m-%d"
    return {
        "name": name,
        "born_year": byear.strftime(date_format), 
        "application_year": ayear.strftime(date_format),
        "graduation_year": (ayear + study3y9m).strftime(date_format),
        "scholarship": None,
        "grades": grades,
        "average_grade": round(sum(grades)/len(grades), 2)
    }


def calc_sholarship() -> list:
    db_is_loaded()
    students = DB["students"]
    students = sorted(students,
                      key=lambda s: s["average_grade"],
                      reverse=True)

    unrated = 0
    for s in students:
        if s["average_grade"] < 60.0:
            s["scholarship"] = "Unrated"
            unrated += 1

    rated = len(students) - unrated
    common_s = int(rated * 0.4) 
    increased_s = int(common_s * 0.2)

    for rating, s in enumerate(students[:rated]):
        if rating <= increased_s:
            s["scholarship"] = "Increased"
        elif rating <= common_s:
            s["scholarship"] = "Common"
        else:
            s["scholarship"] = "None"

    DB["students"] = students
    return deepcopy(students)


def get_students() -> list[dict]:
    db_is_loaded()
    return calc_sholarship()


def get_student(id: int):
    db_is_loaded()
    return deepcopy(DB["students"][id])


def update_student(id: int, student: dict):
    db_is_loaded()
    DB["students"][id] = deepcopy(student)
    calc_sholarship()
    save()


def append_student(student: dict) -> int:
    db_is_loaded()
    DB["students"].append(deepcopy(student))
    save()
    return len(DB["students"])-1


def pop_student(id: int) -> dict:
    db_is_loaded()
    student = DB["students"].pop(id)
    save()
    return deepcopy(student)


def random_student() -> dict:
    FIRSTNAMES = ["James", "Michal", "Robert", "Jonh", "David", "William",
                  "Richard", "Joseph", "Thomas", "Mary", "Julia", "Linda",
                  "Lisa", "Nancy", "Laura", "Deborah", "Sandra", "Maria"]
    LASTNAMES = ["Smith", "Johnson", "Williams", "Brown", "Miller", "Davis",
                "Jones", "Anderson", "Jackson", "Martin", "Moore", "Martinez",
                "Lopez", "Nelson", "Adams", "Mitchell"]

    from random import choice, randint

    name = " ".join([choice(FIRSTNAMES), choice(LASTNAMES)]) 
    byear = datetime.now() - timedelta(days=365*19 + randint(-100, 100))
    ayear = datetime.now()
    grades = [randint(0, 100) for _ in SUBJECTS]

    return student(name, byear, ayear, grades)


def random_db(size: int):
    for _ in range(size):
        s = random_student()
        append_student(s)


# Load DB when module using
load()

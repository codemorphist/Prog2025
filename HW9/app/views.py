"""
This is file for you views functions
"""

from app.responce import Responce, HTMLResponce
from app.errors import responce_400, responce_404
import app.db as db

from datetime import datetime


def index(path, data):
    return HTMLResponce("index.html")


def view_student(path, data, id: int):
    subjects = db.get_subjects()
    try:
        student = db.get_student(id)
        student["id"] = id
    except:
        return responce_404("Student not found")

    return HTMLResponce("student.html", 
                        context={"student": student,
                                 "subjects": subjects})


def delete_student(path, data, id: int):
    try:
        student = db.pop_student(id)
    except:
        return responce_404()
    return HTMLResponce("deleted.html", 
                        context={"student": student})


def view_students(path, data):
    subjects = db.get_subjects()
    students = db.get_students()
    return HTMLResponce("view_students.html",
                        context={"subjects": subjects,
                                 "students": students})


def parse_student(data) -> dict | Responce:
    subjects = db.get_subjects()
    keys = ["name", "byear", "ayear"] 
    s_keys = [f"subject-{i}" for i in range(len(subjects))]

    for key in keys + s_keys:
        if key not in data:
            return responce_400(f"{key} not defined")

    data["name"] = data["name"].strip()
    if data["name"] == "":
        return responce_400(f"Name can't be empty")

    grades = [0] * len(subjects)
    for key, value in data.items():
        if key.startswith("subject-"):
            si = int(key.split("subject-")[1])
            grades[si] = int(value)
        elif key.endswith("year"):
            data[key] = datetime.strptime(data[key], "%Y-%m-%d")
        elif key not in keys:
            return responce_400(f"Invalid key {key}")

    for key in s_keys:
        del data[key]

    data["grades"] = grades

    s = db.student(**data)
    id = db.append_student(s)

    s["id"] = id

    return s


def add_student(path, data):
    subjects = db.get_subjects()
    if data == {}:
        return HTMLResponce("add_student.html",
                            context={"subjects": subjects})
    
    res = parse_student(data)
    if isinstance(res, Responce):
        return res

    student = res

    return HTMLResponce("added.html", context={"subjects": subjects, 
                                               "student": student})


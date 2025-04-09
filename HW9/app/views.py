"""
This is file for you views functions
"""

from app.http import StatusCode
from app.responce import HTMLResponce, HttpResponce
from app.responce import JSONResponce
from app.templates import render

from app.errors import responce_404, responce_500

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
        return responce_404("Student not found")
    return HTMLResponce("deleted.html", 
                        context={"student": student})


def view_students(path, data):
    subjects = db.get_subjects()
    students = db.get_students()
    return HTMLResponce("view_students.html",
                        context={"subjects": subjects,
                                 "students": students})


def add_student(path, data):
    subjects = db.get_subjects()
    if data == {}:
        return HTMLResponce("add_student.html",
                            context={"subjects": subjects})

    grades = [0] * len(subjects)
    for key, value in data.items():
        if key.startswith("subject-"):
            si = int(key.split("subject-")[1])
            grades[si] = int(value)
        elif key.endswith("year"):
            data[key] = datetime.strptime(data[key], "%Y-%m-%d")

    for key in list(data.keys()):
        if key.startswith("subject-"):
            del data[key]

    data["grades"] = grades

    s = db.student(**data)
    db.append_student(s)

    return HTMLResponce("added.html", context={"subjects": subjects, 
                                               "student": s})

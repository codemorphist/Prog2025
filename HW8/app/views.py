"""
This is file for you views functions
"""

from app.responce import HTMLResponce, HttpResponce
from app.responce import JSONResponce
from app.templates import render

import json
import app.db as db


def index(path, params):
    return HTMLResponce("index.html")


def add(path, params):
    if params == {}:
        return HTMLResponce("add.html")
    else:
        toy = {
            "name": params["name"],
            "price": float(params["price"]),
            "age_range": [params["age-from"], params["age-to"]]
        }
        db.insert(toy)
        db.save()
        return HTMLResponce("added.html", context={"toy": toy})


def view(path, params):
    toys = db.get_toys()
    print(toys)
    return HTMLResponce("view.html", context={"toys": toys})


def toys_filter_age(from_age: int, to_age: int):
    def _filter(obj: dict):
        obj_from, obj_to = map(int, obj["age_range"])
        return from_age <= obj_from and obj_to <= to_age
    return _filter


def get_toys(path, params):
    toys = db.get_toys()
    print(params)
    if "range" in params:
        from_age, to_age = list(map(int, params["range"].split()))
        iterator = filter(toys_filter_age(from_age, to_age), toys)
        toys = list(iterator)
    json_data = json.dumps(toys, indent=4)
    return JSONResponce(json_data)

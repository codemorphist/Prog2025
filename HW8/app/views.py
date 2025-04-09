"""
This is file for you views functions
"""

from app.http import StatusCode
from app.responce import HTMLResponce, HttpResponce
from app.responce import JSONResponce
from app.templates import render

from app.errors import responce_400, responce_500

import json
import app.db as db


def index(path, data):
    return HTMLResponce("index.html")


def add_toy(path, data):
    if data == {}:
        return HTMLResponce("add.html")
    else:
        for param in ["name", "price", "age"]:
            if param not in data:
                return responce_400(f"Parameter [{param}] not given")

        toy = {
            "name": data["name"],
            "price": float(data["price"]),
            "age": data["age"]
        }
        db.insert(toy)
        db.save()
        return HTMLResponce("added.html", context={"toy": toy})


def delete_toy(path, data, toy_id: int):
    try:
        toy_id = path.split("/")[-1]
        toy_index = int(toy_id)
        toy = db.delete_toy(toy_index)
    except:
        return responce_500() 

    return HTMLResponce("deleted.html", 
                        context={"toy": toy})

def view_toys(path, data):
    toys = db.get_toys()
    return HTMLResponce("view.html", context={"toys": toys})


def filter_toys(path, data):
    return HTMLResponce("filter.html")


def toys_age_filter(min_age: int, max_age: int):
    def _filter(obj: dict):
        obj_age = int(obj["age"])
        return min_age <= obj_age <= max_age
    return _filter


def get_toys(path, data):
    toys = db.get_toys()
    if "min-age" in data and "max-age" in data:
        min_age = int(data["min-age"])
        max_age = int(data["max-age"])
        filtered = filter(toys_age_filter(min_age, max_age), toys)
        toys = list(filtered)

    json_data = json.dumps(toys, indent=4)
    return JSONResponce(json_data)

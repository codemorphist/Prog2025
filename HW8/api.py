from http_utils import StatusCode
from responce import HTMLResponce, HttpResponce
from templates import render

import json_db


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
        json_db.insert(toy)
        return HTMLResponce("added.html", context={"toy": toy})


def view(path, params):
    toys = json_db.get_toys()
    return HTMLResponce("view.html", context={"toys": toys})

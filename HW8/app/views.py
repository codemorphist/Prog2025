from app.utils import StatusCode
from app.utils import contenttype_html
from app.responce import HTMLResponce, HttpResponce
from app.templates import render

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
    return HTMLResponce("view.html", context={"toys": toys})

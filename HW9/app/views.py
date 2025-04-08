"""
This is file for you views functions
"""

from app.http import StatusCode
from app.responce import HTMLResponce, HttpResponce
from app.responce import JSONResponce
from app.templates import render

from app.errors import responce_400, responce_500

import app.db as db


def index(path, data):
    return HTMLResponce("index.html")



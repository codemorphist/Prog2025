from http_utils import StatusCode
from responce import HTMLResponce, HttpResponce


def index(path, params):
    return HTMLResponce("index.html")


def add(path, params):
    print(params)
    return HttpResponce("This is add")


def view(path, params):
    print(params)
    return HttpResponce("This is view")

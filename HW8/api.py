from http_utils import StatusCode
from responce import Responce 


def add(path, params) -> Responce:
    print(params)
    return StatusCode.S200, "This is add"


def view(path, params) -> Responce:
    print(params)
    return StatusCode.S200, "This is view"

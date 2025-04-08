from enum import Enum


class StatusCode(str, Enum):
    S200 = "200 OK"
    S400 = "400 BAD REQUEST"
    S404 = "404 NOT FOUND"


contenttype_html = ("Content-Type", "text/html; charset=utf-8")

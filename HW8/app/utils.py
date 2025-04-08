from enum import Enum


class StatusCode(str, Enum):
    S200 = "200 OK"
    S400 = "400 BAD REQUEST"
    S404 = "404 NOT FOUND"
    S500 = "500 INTERNAL SERVER ERROR"


contenttype_text = ("Content-Type", "text/plain; charset=utf-8")
contenttype_html = ("content-type", "text/html; charset=utf-8")
contenttype_json = ("Content-Type", "application/json; charset=utf-8")
contenttype_xml  = ("Content-Type", "text/xml; charset=utf-8")


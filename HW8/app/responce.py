from typing import List, TypeAlias, Tuple, AnyStr, Iterator

from app.utils import StatusCode
from app.utils import *
from app.templates import render

Headers: TypeAlias = List[Tuple[AnyStr, AnyStr]]


class Responce:
    def __init__(self, 
                 body: str, 
                 status: StatusCode = StatusCode.S200, 
                 headers: Headers = [contenttype_text]):
        self.body = body
        self.status = status
        self.headers = headers

    def __iter__(self) -> Iterator:
        yield self.status.value
        yield [*self.headers]
        yield self.body


class HttpResponce(Responce):
    def __init__(self, 
                 body: str, 
                 status: StatusCode = StatusCode.S200, 
                 headers: Headers = [contenttype_html]):
        super().__init__(body, status, headers)


class HTMLResponce(HttpResponce):
    def __init__(self, 
                 template: str,  
                 context: dict = {}, 
                 status: StatusCode = StatusCode.S200,
                 headers: Headers = [contenttype_html]):
        body = render(template, **context)
        super().__init__(body, status, headers)


class JSONResponce(Responce):
    def __init__(self, 
                 json: str, 
                 status: StatusCode = StatusCode.S200,
                 headers: Headers = [contenttype_json]):
        super().__init__(json, status, headers)

from http_utils import StatusCode, contenttype_html
from typing import List, TypeAlias, Tuple, AnyStr, Iterator

from templates import render

Responce: TypeAlias = Tuple[StatusCode, AnyStr]
Headers: TypeAlias = List[Tuple[AnyStr, AnyStr]]


class HttpResponce:
    def __init__(self, 
                 body: str, 
                 status: StatusCode = StatusCode.S200, 
                 headers: Headers = [contenttype_html]):
        self.body = body
        self.status = status
        self.headers = headers

    def __iter__(self) -> Iterator:
        yield self.status
        yield self.headers
        yield self.body


class HTMLResponce(HttpResponce):
    def __init__(self, 
                 template: str,  
                 context: dict = {}, 
                 status: StatusCode = StatusCode.S200,
                 headers: Headers = [contenttype_html]):
        body = render(template, **context)
        super().__init__(body, status, headers)


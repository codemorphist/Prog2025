"""
This module contains responce classes to fast generate responce
from view function
"""

from typing import List, TypeAlias, Tuple, AnyStr, Iterator

from app.utils import StatusCode
from app.utils import *
from app.templates import render

import json


Headers: TypeAlias = List[Tuple[AnyStr, AnyStr]]


class Responce:
    """
    Implement basic responce with 
    Contenty-Type: plain/text; charset=utf-8
    """
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
    """
    Impletent HTML responce
    """
    def __init__(self, 
                 body: str, 
                 status: StatusCode = StatusCode.S200, 
                 headers: Headers = [contenttype_html]):
        super().__init__(body, status, headers)


class HTMLResponce(HttpResponce):
    """
    Implemtent HTML responce from template

    context is dict with values for template
    """
    def __init__(self, 
                 template: str,  
                 context: dict = {}, 
                 status: StatusCode = StatusCode.S200,
                 headers: Headers = [contenttype_html]):
        body = render(template, **context)
        super().__init__(body, status, headers)


class JSONResponce(Responce):
    """
    Implement JSON responce

    json_format is parameters for json.dumps
    """
    def __init__(self, 
                 json_data: str, 
                 status: StatusCode = StatusCode.S200,
                 headers: Headers = [contenttype_json],
                 **json_format):
        body = json_data
        if json_format:
            body = json.dumps(json.loads(json_data), **json_format)

        super().__init__(body, status, headers)


class XMLResponce(Responce):
    """
    Implement XML responce
    """
    def __init__(self,
                 xml_data: str,
                 status: StatusCode = StatusCode.S200,
                 headers: Headers = [contenttype_xml]):
        body = xml_data

        super().__init__(body, status, headers)

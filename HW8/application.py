import urllib.parse

from http_utils import StatusCode
from http_utils import contenttype_html

from urls import urlpatterns, compare_pattern

from templates import render


def application(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")
    
    query_string = environ.get("QUERY_STRING", "")
    params = urllib.parse.parse_qs(query_string)

    for pattern, view in urlpatterns:
        if compare_pattern(path, pattern):
            status, body = view(path, params)
            break
    else:
        status = StatusCode.S404
        body = render("404.html", path=path)

    start_response(status.value, [contenttype_html])
    return [bytes(body, encoding="utf-8")]

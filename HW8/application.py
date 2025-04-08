import urllib.parse

from http_utils import StatusCode
from responce import HTMLResponce

from urls import urlpatterns, compare_pattern


def application(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")
    
    query_string = environ.get("QUERY_STRING", "")
    params = urllib.parse.parse_qs(query_string)

    for pattern, view in urlpatterns:
        if compare_pattern(path, pattern):
            status, headers, body = view(path, params)
            break
    else:
        status, headers, body = HTMLResponce("404.html", 
                                             status=StatusCode.S404)

    start_response(status.value, headers)
    return [bytes(body, encoding="utf-8")]

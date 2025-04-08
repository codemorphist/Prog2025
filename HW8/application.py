import urllib.parse

from http_utils import StatusCode
from responce import HTMLResponce

from urls import urlpatterns, compare_pattern

from wsgiref.headers import Headers


def application(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")
    
    query_string = environ.get("QUERY_STRING", "")
    params = urllib.parse.parse_qs(query_string)

    length = environ.get('CONTENT_LENGTH', '0')
    try:
        length = int(length)
    except ValueError:
        length = 0

    raw_post_data = environ["wsgi.input"].read(length) if length > 1 else b""

    params = {}
    if raw_post_data:
        parsed_data = urllib.parse.parse_qs(raw_post_data.decode("utf-8"))
        params = {key: value[0] for key, value in parsed_data.items()}

    status, headers, body = HTMLResponce("404.html", 
                                         status=StatusCode.S404)
    for pattern, view in urlpatterns:
        if compare_pattern(path, pattern):
            status, headers, body = view(path, params)
            break

    headers = [*headers] # ? BUG AND HARDCODE
    start_response(status.value, headers)
    return [bytes(body, encoding="utf-8")]

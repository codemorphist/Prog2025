import urllib.parse

from app.utils import StatusCode
from app.responce import HTMLResponce

from app.urls import urlpatterns, compare_pattern

import traceback


def application(environ, start_response):
    # Get request path
    path = environ.get("PATH_INFO", "").lstrip("/")
    
    length = environ.get('CONTENT_LENGTH', '0')
    try:
        length = int(length)
    except ValueError:
        length = 0

    raw_post_data = environ["wsgi.input"].read(length) if length > 1 else b""

    # Parse params form from (if exist)
    params = {}
    if raw_post_data:
        parsed_data = urllib.parse.parse_qs(raw_post_data.decode("utf-8"))
        params = {key: value[0] for key, value in parsed_data.items()}

    # Default responce 404 HTTP Error
    status, headers, body = HTMLResponce("404.html", 
                                         status=StatusCode.S404)

    for pattern, view in urlpatterns:
        if compare_pattern(path, pattern):
            try: # If patter found generate responce
                status, headers, body = view(path, params)
            except Exception as e: # If Exception return 500 HTTP error
                status, headers, body = HTMLResponce(
                        "500.html", 
                        status=StatusCode.S500,
                        context={"error": traceback.format_exc()}
                    )
            finally:
                break

    start_response(status, headers)
    return [bytes(body, encoding="utf-8")]

"""
This is main file that contain implementaion of
WSGI application
"""

import urllib.parse

from app.errors import responce_404, responce_500
from app.urls import urlpatterns

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
    data = {}
    if raw_post_data:
        parsed_data = urllib.parse.parse_qs(raw_post_data.decode("utf-8"))
        data = {key: value[0] for key, value in parsed_data.items()}

    # Default responce 404 HTTP Error
    status, headers, body = responce_404(path)

    for pattern in urlpatterns:
        matched, params = pattern.parse(path) 
        if matched:
            try: # If patter found generate responce
                status, headers, body = pattern.view(path, data, **params)
            except Exception as e: # If Exception return 500 HTTP error
                error = traceback.format_exc()
                status, headers, body = responce_500(error)      
            finally:
                break

    start_response(status, headers)
    return [bytes(body, encoding="utf-8")]

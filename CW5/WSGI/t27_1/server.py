from wsgiref.simple_server import make_server


def application(environ, start_responce):
    if environ.get("PATH_INFO", "").lstrip("/") == "":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], 
                                environ=environ)
        body = "" 
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    else:
        start_response("404 NOT FOUND", [("Content-Type", "text/plain")])
        body = "" 
    return [bytes(body, encoding="utf-8")]


if __name__ == "__main__":
    httpd = make_server("localhost", 8051, application)
    httpd.serve_forever()

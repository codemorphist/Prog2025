import cgi
from wsgiref.simple_server import make_server
from jinja2 import Template
from seq import count_sign_change


def application(environ, start_response):
    with open("index.html", "r") as html:
        index = Template(html.read())

    path = environ.get("PATH_INFO", "").lstrip("/")
    body = ""

    if path == "":
        body = index.render()
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    elif path == "count-sign-change":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], 
                                environ=environ)
        if "seq" in form:
            seq = form["seq"].value

            try:
                res = count_sign_change(seq)
                body = index.render(result=f"Result: {res}")
                status_code = "200 OK"
            except Exception as e:
                body = index.render(error=f"Exception: {e}")
                status_code = "400 BAD REQUEST"
        else:
            body = index.render(exception=f"Exception: {e}")
            status_code = "400 BAD REQUEST"

        mimetype = "text/html"
        start_response(status_code, [("Content-Type", f"{mimetype}; charset=utf-8")])
    elif path.startswith("static/"):
        with open(path, "r") as f:
            body = f.read()
        start_response("200 OK", [("Content-Type", "text/css")])
    else:
        start_response("404 NOT FOUND", [("Content-Type", "text/plain")])
        body = "[404] Page not found"
    return [bytes(body, encoding="utf-8")]


if __name__ == "__main__":
    print("=== Local WSGI webserver ===")
    with make_server("0.0.0.0", 8000, application) as httpd:
        httpd.serve_forever()

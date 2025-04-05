import cgi
from wsgiref.simple_server import make_server
from jinja2 import Template
import db


def application(environ, start_response):
    with open("index.html", "r") as html:
        index = Template(html.read())

    path = environ.get("PATH_INFO", "").lstrip("/")
    body = ""

    if path == "":
        body = index.render(currency=db.get_currency())
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    elif path == "convert-currency":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], 
                                environ=environ) 

        cur = form["currency"].value
        from_cur, to_cur = cur.split("/")
        amount = float(form["amount"].value)
        new_amount = db.convert(amount, cur)

        result = f"{amount:.2f} {from_cur} -> {new_amount:.2f} {to_cur}"
        body = index.render(currency=db.get_currency(), result=result)
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
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
        db.load_currency() # load database
        httpd.serve_forever() # start server

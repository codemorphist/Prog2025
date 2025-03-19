import cgi
from wsgiref.simple_server import make_server
import wordcount


def application(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")
    if path == "":
        with open("index.html", "r") as html:
            body = html.read()    
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    elif path == "get-json":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], 
                                environ=environ)
        body = ""
        if "url" in form:
            url = form["url"].value
            html = wordcount.get_html(url)
            counts = wordcount.wordcount(html)
            body = wordcount.generate_wordcount_json(counts)
        start_response("200 OK", [("Content-Type", "application/json; charset=utf-8")])
    else:
        # якщо команда невідома, то виникла помилка
        start_response("404 NOT FOUND", [("Content-Type", "text/plain")])
        body = "[404] Page not found"
    return [bytes(body, encoding="utf-8")]


if __name__ == "__main__":
    print("=== Local WSGI webserver ===")
    httpd = make_server("localhost", 8000, application)
    httpd.serve_forever()

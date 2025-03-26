import cgi
from wsgiref.simple_server import make_server
import wordcount


def application(environ, start_response):
    path = environ.get("PATH_INFO", "").lstrip("/")
    if path == "":
        with open("index.html", "r") as html:
            body = html.read()    
        start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    elif path == "count-words":
        form = cgi.FieldStorage(fp=environ["wsgi.input"], 
                                environ=environ)
        body = ""
        if "url" in form:
            url = form["url"].value
            html = wordcount.get_html(url)
            counts = wordcount.wordcount(html)
        if "get-json" in form:
            mimetype = "application/json"
            body = wordcount.generate_wordcount_json(counts)
        elif "get-xml" in form:
            print("XML")
            mimetype = "text/xml"
            body = wordcount.generate_wordcount_xml(counts)
        else:
            mimetype = "text/plain"
            body = "Invalid format type"
        start_response("200 OK", [("Content-Type", f"{mimetype}; charset=utf-8")])
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

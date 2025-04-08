from wsgiref.simple_server import make_server

from app.wsgi import application


if __name__ == "__main__":
    print("=== Local WSGI webserver ===")
    with make_server("0.0.0.0", 8000, application) as httpd:
        httpd.serve_forever() # start server

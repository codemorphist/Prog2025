from http.server import HTTPServer, CGIHTTPRequestHandler

if __name__ == "__main__":
    print("=== LOCAL WEBSERVER STARTED ===")
    HOST, PORT = "localhost", 8888
    with HTTPServer((HOST, PORT), CGIHTTPRequestHandler) as s:
        s.serve_forever()

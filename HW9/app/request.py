import cgi
from urllib.parse import parse_qs, urlparse


class Request:
    def __init__(self, environ):
        self.environ = environ
        self.method = environ.get('REQUEST_METHOD', 'GET')
        self.path = environ.get('PATH_INFO', '')
        self.query_string = environ.get('QUERY_STRING', '')
        self.headers = self._parse_headers(environ)
        self.body = self._get_request_body(environ)
        self.form = self._parse_form_data(environ)
        self.client_ip = self._get_client_ip(environ)
        self.server_name = environ.get('SERVER_NAME', '')
        self.server_port = environ.get('SERVER_PORT', '')

    def _parse_headers(self, environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                header_name = key[5:].replace('_', '-').title()
                headers[header_name] = value
        return headers

    def _get_request_body(self, environ):
        if environ.get('REQUEST_METHOD') in ['POST', 'PUT', 'PATCH']:
            return environ['wsgi.input'].read(int(environ.get('CONTENT_LENGTH', 0)))
        return b''

    def _parse_form_data(self, environ):
        form_data = {}
        content_type = self.headers.get('Content-Type', '').lower()

        # Parse application/x-www-form-urlencoded (default for form submissions)
        if content_type.startswith('application/x-www-form-urlencoded'):
            form_data = parse_qs(self.query_string)

        # Parse multipart form data (for file uploads)
        elif content_type.startswith('multipart/form-data'):
            fs = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)
            for field in fs.keys():
                item = fs[field]
                if item.filename:
                    form_data[field] = item
                else:
                    form_data[field] = item.value

        return form_data

    def _get_client_ip(self, environ):
        # Try to get the client IP from the HTTP_X_FORWARDED_FOR header (common with reverse proxies)
        forwarded_for = self.headers.get('X-Forwarded-For', '')
        if forwarded_for:
            return forwarded_for.split(',')[0].strip()
        return environ.get('REMOTE_ADDR', '')

    def get_query_params(self):
        # Parse the query string into a dictionary
        return parse_qs(self.query_string)

    def __str__(self):
        return f"Request({self.method} {self.path})"


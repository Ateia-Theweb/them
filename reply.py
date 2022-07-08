from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

host = 'localhost'
port = 8000

server_address = (host, port)

name = 'RequestHandlerClass'
base = (BaseHTTPRequestHandler,)


def get(self):
    headerk = 'Content-Type'
    headerv = 'Text/HTML'
    ok = 200

    self.send_response(ok)

    self.send_header(headerk, headerv)
    self.end_headers()

    self.wfile.write(b'Reply')  # HARDCODED


meth = {
    'do_GET': get,

}

RequestHandlerClass = type(name, base, meth)

with HTTPServer(server_address, RequestHandlerClass) as httpd:
    httpd.handle_request()

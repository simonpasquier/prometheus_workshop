#!/usr/bin/env python
import random
import time


from http.server import BaseHTTPRequestHandler, HTTPServer


def metrics(self):
    self.send_response(404)


def not_found(self):
    self.send_response(404)


def error(self):
    self.send_response(500)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write(bytes("Server error", "utf8"))


def home(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    message = "Hello {}!\n".format(self.address_string())
    self.wfile.write(bytes(message, "utf8"))
    # Add an artifical delay before responding to the client
    time.sleep(random.random())
    return


ROUTES = {
    '/': home,
    '/error': error,
    '/metrics': metrics
}


# Class handling HTTP requests
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        return ROUTES.get(self.path, not_found)(self)


def run():
  print('starting server...')

  server_address = ('127.0.0.1', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()

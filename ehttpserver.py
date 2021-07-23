#!/usr/bin/python3

import http.server
import socketserver
import argparse
import os

PORT = 8000

class ExtendedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, **kwargs)

    def do_PUT(self):
        """Serve a PUT request."""
        try:
            path = self.translate_path(self.path)
            length = int(self.headers["Content-Length"])
            if False: 
                pass # for future input validation
            else:
                with open(path, 'wb') as fh:
                    fh.write(self.rfile.read(length))
                self.send_response(201, "Created")
                self.end_headers()
        except:
            self.send_response(500, "Internal Server Error")
            self.end_headers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extended HTTP Server by w0lfram1te')
    parser.add_argument('port', metavar='port', type=int, nargs='?', default=8000, help="listening port")
    parser.add_argument('-b','--bind', action='store', dest='bind', default='0.0.0.0', help="bind address")
    parser.add_argument('-p', '--port', action='store', dest='port', default=8000, help="listening port")
    args = parser.parse_args()

    print("[*] Running Extended HTTP Server by w0lfram1te")
    http.server.test(HandlerClass=ExtendedHTTPRequestHandler, port=args.port, bind=args.bind)
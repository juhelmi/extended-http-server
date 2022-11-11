#!/usr/bin/python3

import http.server
import argparse
import urllib
import io
import json
import traceback


class ExtendedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, **kwargs)

    def do_PUT(self):
        """Serve a PUT request."""
        try:
            path = self.translate_path(self.path)
            length = int(self.headers["Content-Length"])
            if False: 
                pass  # for future input validation
            else:
                with open(path, 'wb') as fh:
                    fh.write(self.rfile.read(length))
                self.send_response(201, "Created")
                self.end_headers()
        except:
            self.send_response(500, "Internal Server Error")
            self.end_headers

    def do_POST(self):
        path = self.translate_path(self.path)
        print(f'POST path {path}')
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        print(f'Body json: {body}')
        # https://copyprogramming.com/tutorial/python-http-server-response
        try:
            # result = json.loads(body, encoding='utf-8')
            result = json.loads(body)
            # Do other stuff with result
            self.send_response(200)
            self.end_headers()
            response = io.BytesIO()
            # response.write(b'POST Received length: ')
            # s_len = str(len(body))
            # response.write(bytes(s_len, 'utf-8'))
            response.write(b'POST')
            # response.write(b'POST Received: ')
            # response.write(body)
            self.wfile.write(response.getvalue())
            print(f'Result json was: {result}')
            for key in result:
                if len(result[key]) > 0:
                    print(f'{key}={result[key]}')
        except Exception as err:
            print(f'Error {err}')
            tb = traceback.format_exc()
            print(tb)
            self.send_response(500)  # 500 Internal Server Error
            self.end_headers()
            response = io.BytesIO()
            response.write(b'ERROR: Blah, reason not identified')
            self.wfile.write(response.getvalue())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extended HTTP Server by w0lfram1te')
    parser.add_argument('port', metavar='port', type=int, nargs='?', default=8088, help="listening port")
    parser.add_argument('-b', '--bind', action='store', dest='bind', default='0.0.0.0', help="bind address")
    parser.add_argument('-p', '--port', action='store', dest='port', default=8088, help="listening port")
    args = parser.parse_args()

    print("[*] Running Extended HTTP Server by w0lfram1te")
    http.server.test(HandlerClass=ExtendedHTTPRequestHandler, port=args.port, bind=args.bind)

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
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        if False:
            print(f'Plain data: {body}')
            post_data = urllib.parse.parse_qs(body.decode('utf-8'))
            # post_data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
            # You now have a dictionary of the post data
            print(f'Polku on {self.path}')
            f = open('tuleva.txt', "w")
            s = str(post_data)
            f.write(s)
            f.close()

            # self.wfile.write("Lorem Ipsum".encode("utf-8"))
            self.wfile.write("OK".encode("utf-8"))
        elif True:
            # https://copyprogramming.com/tutorial/python-http-server-response
            try:
                # result = json.loads(body, encoding='utf-8')
                result = json.loads(body)
                # Do other stuff with result
                self.send_response(200)
                self.end_headers()
                response = io.BytesIO()
                response.write(b'POST Received: ')
                response.write(body)
                self.wfile.write(response.getvalue())
            except Exception as err:
                tb = traceback.format_exc()
                print(tb)
                self.send_response(500)  # 500 Internal Server Error
                self.end_headers()
                response = io.BytesIO()
                response.write(b'ERROR: Blah')
                self.wfile.write(response.getvalue())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extended HTTP Server by w0lfram1te')
    parser.add_argument('port', metavar='port', type=int, nargs='?', default=8088, help="listening port")
    parser.add_argument('-b', '--bind', action='store', dest='bind', default='0.0.0.0', help="bind address")
    parser.add_argument('-p', '--port', action='store', dest='port', default=8088, help="listening port")
    args = parser.parse_args()

    print("[*] Running Extended HTTP Server by w0lfram1te")
    http.server.test(HandlerClass=ExtendedHTTPRequestHandler, port=args.port, bind=args.bind)

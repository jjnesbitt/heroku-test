# Python 3 server example
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from test import __version__

serverPort = int(os.getenv("PORT", "8080"))


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(__version__))


if __name__ == "__main__":
    webServer = HTTPServer(("", serverPort), MyServer)
    print("Server started on port %s" % serverPort)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

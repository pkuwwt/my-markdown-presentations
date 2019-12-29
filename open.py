import os
import sys
from os.path import join, isfile, isdir
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port

def is_presentation(path):
    if isfile(path) and path.endswith('.md'):
        return True
    if isdir(path) and isfile(join(path, 'README.md')):
        return True
    return False

class Redirect(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        port = self.connection.getsockname()[1]
        if is_presentation(self.path[1:]):
            url = 'http://127.0.0.1:{}/render/index.html?file={}'.format(port, path)
            print(url)
            self.send_response(302)
            self.send_header('Location', url)
            self.end_headers()
        else:
            super().do_GET()

def serve(path, port):
    root_path = os.path.abspath(path)
    print(path)
    print('Serve files in {} on http://127.0.0.1:{}'.format(root_path, port))
    os.chdir(root_path)
    TCPServer(("", int(port)), Redirect).serve_forever()

def serve_with_open_port(path):
    port = get_open_port()
    serve(path, port)

def main():
    if len(sys.argv) == 1:
        serve_with_open_port('.')
    else:
        serve_with_open_port(sys.argv[1])

if __name__ == '__main__':
    main()


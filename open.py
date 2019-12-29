import os
import sys
from os.path import join, isfile, isdir, abspath, dirname
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import socket

default_port = 8080

def get_script_dir():
    return dirname(abspath(sys.argv[0]))

root = get_script_dir()

def is_port_in_use(port):
    used = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("", port))
        s.listen(1)
    except Exception as e:
        used = True
    finally:
        s.close()
    return used

def get_open_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port

def try_port(port):
    if is_port_in_use(port):
        return get_open_port()
    return port

def is_presentation(path):
    path = join(root, path)
    if isfile(path) and path.endswith('.md'):
        return True
    return False

class Redirect(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=root, **kwargs)
    def do_GET(self):
        path = self.path
        port = self.connection.getsockname()[1]
        if is_presentation(self.path[1:]):
            url = 'http://127.0.0.1:{}/render/index.html?file={}'.format(port, path)
            self.send_response(302)
            self.send_header('Location', url)
            self.end_headers()
        else:
            super().do_GET()

def serve(port):
    print('Serve files in {} on http://127.0.0.1:{}'.format(root, port))
    TCPServer(("", int(port)), Redirect).serve_forever()

def serve_with_open_port():
    port = try_port(default_port)
    serve(port)

def main():
    serve_with_open_port()

if __name__ == '__main__':
    main()


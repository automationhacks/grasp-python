import re
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from threading import Thread

import requests


class MockServerRequestHandler(BaseHTTPRequestHandler):
    USERS_PATTERN = re.compile(r'/users')

    def do_GET(self):
        if re.search(self.USERS_PATTERN, self.path):
            self.send_response(requests.codes.ok)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            mock_data_path = get_mocked_json_response()

            with open(mock_data_path) as f:
                response_content = f.read()

            self.wfile.write(response_content.encode('utf-8'))

            return


def get_mocked_json_response():
    return str(
        [path for path in Path('../../..').glob('**/users.json')][0])


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()

    return port


def start_mock_server(port):
    print('Starting mock server at localhost:{}'.format(port))
    mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()

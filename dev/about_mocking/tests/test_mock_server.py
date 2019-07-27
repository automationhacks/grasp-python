import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

import requests
from nose.tools import assert_true

"""
Steps to writing a mock:

1. Subclass BaseHTTPRequestHandler from http.server module
2. Override the HTTP function to send your response
3. Get a free port via socket module
4. Create an instance of HTTPServer from http.server module
5. Create a Thread to start this HTTPServer in
6. Make this thread as daemon so that it terminates when the main program exits
7. Start the mock server before the test
8. Run the test.
"""


class MockServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(requests.codes.ok)
        self.end_headers()

        return


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()

    return port


class TestMockServer:

    @classmethod
    def setup_class(cls):
        cls.mock_server_port = get_free_port()
        cls.mock_server = HTTPServer(('localhost', cls.mock_server_port),
                                     MockServerRequestHandler)

        cls.mock_server_thread = Thread(target=cls.mock_server.serve_forever)
        cls.mock_server_thread.setDaemon(True)
        cls.mock_server_thread.start()

    def test_request_response(self):
        url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        response = requests.get(url)
        assert_true(response.ok)

import socket


class client():
    """docstring for client."""
    def __init__(self):
        self.sock = None

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host=socket.gethostname(), port=8880):
        if host is None:
            self.sock.connect((host, port))
        else:
            self.sock.connect((host, port))


ok = client()
ok.create_socket()
ok.connect()

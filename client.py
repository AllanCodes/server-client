import socket


class client():
    """Client"""
    def __init__(self):
        self.sock = None

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host=socket.gethostname(), port=8980):
        if host is None:
            self.sock.connect((host, port))
        else:
            self.sock.connect((host, port))

    def send(self):
        while True:
            msg = input("you: ")
            self.sock.sendto(msg.encode(), (socket.gethostname(), 8980))
            print(self.sock.recv(1024).decode())


ok = client()
ok.create_socket()
ok.connect()
ok.send()

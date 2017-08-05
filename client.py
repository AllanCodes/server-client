import socket
import threading


class client():
    """Client"""
    def __init__(self):
        self.sock = None

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host=socket.gethostname(), port=2930):
        if host is None:
            self.sock.connect((host, port))
        else:
            self.sock.connect((host, port))

    def listen(self):
        while True:
            data = self.sock.recv(1024).decode()
            msg = "server: " + data
            print(msg)

    def send(self):
        while True:
            msg = input("you: ")
            self.sock.sendto(msg.encode(), (socket.gethostname(), 2930))

    def handle_threads(self):
        listenThread = threading.Thread(target=self.listen)
        speakThread = threading.Thread(target=self.send)
        listenThread.start()
        speakThread.start()


ok = client()
ok.create_socket()
ok.connect()
ok.handle_threads()

import socket
import threading

class server():
    """docstring for server."""
    def __init__(self):
        self.serversocket = None

    def create_socket(self):
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            self.serversocket.close()

    def bind_socket(self, host=socket.gethostname(), port=8880):
        try:
            self.serversocket.bind((host, port))
        except socket.error:
            self.serversocket.close()

    def listen(self, max=5):
        try:
            self.serversocket.listen(max)
        except socket.error:
            self.serversocket.close()

    def accept(self):
        while True:
            connection = self.serversocket.accept()
            print(connection)


ok = server()
ok.create_socket()
ok.bind_socket()
ok.listen()
ok.accept()
# (clientsocket, address) = serversocket.accept()

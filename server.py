import socket
import threading
import select


class server():
    """threaded server"""
    def __init__(self):
        self.serversocket = None
        self.clientsocket = None
        self.threads = []

    def get_message(self, clientsocket):
        while True:
            data = clientsocket.recv(1024).decode()
            msg = 'server: ' + data
            clientsocket.sendto(msg.encode(), (socket.gethostname(), 8980))
            # data = self.clientsocket.recv(1024).decode()
            # self.clientsocket.sendto(data.encode(), (socket.gethostname(), 8980))

    def create_socket(self):
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("socket error: create")
            self.serversocket.close()

    def bind_socket(self, host=socket.gethostname(), port=8980):
        try:
            self.serversocket.bind((host, port))
        except socket.error:
            print("socket error: bind")
            self.serversocket.close()

    def listen(self, max=5):
        try:
            self.serversocket.listen(max)
        except socket.error:
            print("socket error: listen")
            self.serversocket.close()

    def accept(self):
        while True:
            (self.clientsocket, connection) = self.serversocket.accept()
            print("{} has connected".format(connection))
            self.threads.append(threading.Thread(target=self.get_message, kwargs={'clientsocket': self.clientsocket}))
            self.threads[-1].start()


ok = server()
ok.create_socket()
ok.bind_socket()
ok.listen()
ok.accept()
# (clientsocket, address) = serversocket.accept()

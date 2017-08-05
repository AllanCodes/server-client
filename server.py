import socket
import threading


class server():
    """threaded server"""
    def __init__(self):
        self.serversocket = None
        self.clientsocket = None
        self.threads = []
        self.clientsockets = []

    def get_message(self, clientsocket):
        while True:
            data = clientsocket.recv(1024).decode()
            #msg = 'server: ' + data
            msg = data
            for x in self.clientsockets:
                if x != self.clientsocket:
                    x.sendto(msg.encode(), (socket.gethostname(), 2930))

    def create_socket(self):
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("socket error: create")
            self.serversocket.close()

    def bind_socket(self, host=socket.gethostname(), port=2930):
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
            self.clientsockets.append(self.clientsocket)
            print("{} has connected".format(connection))
            self.threads.append(threading.Thread(target=self.get_message, kwargs={'clientsocket': self.clientsocket}))
            self.threads[-1].start()


ok = server()
ok.create_socket()
ok.bind_socket()
ok.listen()
ok.accept()
# (clientsocket, address) = serversocket.accept()

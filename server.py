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
            msg = data
            self.sendAllClients(clientsocket, msg)

    def sendAllClients(self, clientsocket, msg):
        for x in self.clientsockets:
            if x != clientsocket:
                x.sendto(msg.encode(), (socket.gethostname(), 4444))

    def create_socket(self):
        try:
            self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("socket error: create")
            self.serversocket.close()

    def bind_socket(self, host=socket.gethostname(), port=4444):
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


def runServer():
    serv = server()
    serv.create_socket()
    serv.bind_socket()
    serv.listen()
    serv.accept()

    if __name__ == "__main__":
        pass

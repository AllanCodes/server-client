import server
import client



def runServer():
    serv = server()
    serv.create_socket()
    serv.bind_socket()
    serv.listen()
    serv.accept()

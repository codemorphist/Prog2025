from server import logger, FileTranferServer
from config import *


def echo():
    server = FileTranferServer(HOST, PORT)
    server.accept()
    while True:
        data = server.recv(BUF_SIZE)
        if data == "close server":
            server.close_conn()
            server.close()
            return
        server.send(data)


def test_send_file():
    server = FileTranferServer(HOST, PORT) 
    server.accept()
    server.send_file("_send_file", BUF_SIZE)
    server.close_conn()
    server.close()


def test_recive_file():
    server = FileTranferServer(HOST, PORT) 
    server.accept()
    server.recv_file("_recived_file", BUF_SIZE)
    server.close_conn()
    server.close()


if __name__ == "__main__":
    # echo()
    # test_recive_file()
    test_send_file()


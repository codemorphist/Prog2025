from server import logger, FileTransferServer
from config import *


def echo():
    server = FileTransferServer(HOST, PORT)
    server.accept()
    while True:
        data = server.recv(BUF_SIZE)
        if data == "close server":
            server.close_conn()
            server.close()
            return
        server.send(data)


def test_send_file():
    server = FileTransferServer(HOST, PORT) 
    server.accept()
    server.send_file("_send_file", BUF_SIZE)
    server.close_conn()
    server.close()


def test_recive_file():
    server = FileTransferServer(HOST, PORT) 
    server.accept()
    server.recv_file("_recived_file", BUF_SIZE)
    server.close_conn()
    server.close()

def test_send_file_as():
    server = FileTransferServer(HOST, PORT)
    server.accept()
    server.send_file_as("_send_file", "./server_dir/", BUF_SIZE)
    server.close_conn()
    server.close()


def test_recv_file_as():
    server = FileTransferServer(HOST, PORT)
    server.accept()
    server.recv_file_as(BUF_SIZE)
    server.recv_file_as(BUF_SIZE)
    server.close_conn()
    server.close()


if __name__ == "__main__":
    # echo()
    # test_recive_file()
    # test_send_file()
    test_recv_file_as()
    # test_send_file_as()

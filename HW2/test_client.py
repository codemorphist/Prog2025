from client import logger, FileTransferClient
from config import *


def echo():
    client = FileTransferClient(HOST, PORT)
    client.connect()
    while True:
        data = input("Input data: ").strip()
        if data == "close":
            client.send("close server")
            client.close()
            return
        client.send(data)
        data = client.recv(BUF_SIZE)


def test_send_file():
    client = FileTransferClient(HOST, PORT)
    client.connect()
    client.send_file("_send_file", BUF_SIZE)
    client.close()


def test_recive_file():
    client = FileTransferClient(HOST, PORT)
    client.connect()
    client.recv_file("_recived_file", BUF_SIZE)
    client.close()


def test_send_file_as():
    client = FileTransferClient(HOST, PORT)
    client.connect()
    client.send_file_as("_send_file", "./server_dir/", BUF_SIZE)
    client.send_file_as("_send_file_2", "./server_dir", BUF_SIZE)
    client.close()


def test_recv_file_as():
    client = FileTransferClient(HOST, PORT)
    client.connect()
    client.recv_file_as(BUF_SIZE)
    client.close()


if __name__ == "__main__":
    # echo()
    # test_send_file()
    # test_recive_file()
    test_send_file_as()
    # test_recv_file_as()


from socket_stream import SocketStream
import logging

from config import *

logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
logger = logging.getLogger(__name__)

class FileTransferClient(SocketStream):
    def __init__(self, host: str, port: int):
        super().__init__(host, port, 
                         base_logger=logger)


def test():
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


if __name__ == "__main__":
    test()

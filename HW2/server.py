from socket_stream import SocketStream 
import logging

from config import *

logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
logger = logging.getLogger(__name__)

class FileTranferServer(SocketStream):
    def __init__(self, host: str, port: int):
        super().__init__(host, port,
                      is_server=True,
                      base_logger=logger)
        self.listen()


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


if __name__ == "__main__":
    echo()

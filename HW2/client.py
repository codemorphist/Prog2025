from socket_stream import SocketStream
import logging

from config import *

logging.basicConfig(level=logging.INFO, 
                    format=LOGGING_FORMAT,
                    filename="client.log",
                    filemode="w")
logger = logging.getLogger(__name__)

class FileTransferClient(SocketStream):
    def __init__(self, host: str, port: int):
        super().__init__(host, port, 
                         base_logger=logger)



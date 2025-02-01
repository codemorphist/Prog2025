from socket_stream import SocketStream 
import logging

from config import *

logging.basicConfig(level=logging.INFO, 
                    format=LOGGING_FORMAT,
                    filename="server.log",
                    filemode="w")
logger = logging.getLogger(__name__)

class FileTranferServer(SocketStream):
    def __init__(self, host: str, port: int):
        super().__init__(host, port,
                      is_server=True,
                      base_logger=logger)



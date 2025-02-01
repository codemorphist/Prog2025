from file_transfer import FileTransfer
import logging

from config import LOGGING_FORMAT


logging.basicConfig(level=logging.INFO, 
                    format=LOGGING_FORMAT,
                    filename="server.log",
                    filemode="w")
logger = logging.getLogger(__name__)


class FileTranferServer(FileTransfer):
    def __init__(self, host: str, port: int):
        super().__init__(host, port,
                         is_server=True,
                         base_logger=logger)



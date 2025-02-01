from socket_stream import SocketStream
import logging
import os


class FileTransfer(SocketStream):
    def __init__(self, 
                 host: str, port: int,
                 is_server: bool = False,
                 base_logger: logging.Logger = None):
        super().__init__(host, port,
                         is_server,
                         base_logger)

    def send_file(self, filepath: str, bufsize: int):
        self.logger.info(f"Starting sending file: {filepath}")
        with open(filepath, "rb") as f:
            while chunk := f.read(bufsize):
                self.sendb(chunk)
                self.logger.info(f"Sended: {len(chunk)} bytes of file")
        self.logger.info(f"Ended sending file: {filepath}")

    def recv_file(self, filepath: str, bufsize: int):
        self.logger.info(f"Starting reciving file: {filepath}")
        with open(filepath, "wb") as f:
            while chunk := self.recvb(bufsize):
                f.write(chunk)
                self.logger.info(f"Recived: {len(chunk)} bytes of file")
        self.logger.info(f"Ended reciving file: {filepath}")



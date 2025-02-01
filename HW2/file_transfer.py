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
        self.logger.info(f"BEGIN sending file: {filepath}")
        with open(filepath, "rb") as f:
            while chunk := f.read(bufsize):
                self.sendb(chunk)
                self.logger.info(f"Sended: {len(chunk)} bytes of file")
        self.logger.info(f"END sending file: {filepath}")

    def recv_file(self, filepath: str, bufsize: int):
        self.logger.info(f"BEGIN reciving file: {filepath}")
        with open(filepath, "wb") as f:
            while chunk := self.recvb(bufsize):
                f.write(chunk)
                self.logger.info(f"Recived: {len(chunk)} bytes of file")
        self.logger.info(f"END reciving file: {filepath}")

    def send_file_as(self, filepath: str, savepath: str, bufsize: int):
        self.logger.info(f"BEGIN send file {filepath} and save to {savepath}")
        filename = os.path.basename(filepath)

        self.send_data(filename)
        self.logger.info(f"Sended filename: {filename}")
        
        self.send_data(savepath)
        self.logger.info(f"Sended save path: {savepath}")

        self.send_file(filepath, bufsize)
        self.logger.info(f"END send file {filepath} and save to {savepath}")

    def recv_file_as(self, bufsize: int):
        self.logger.info("BEGIN reciving file as")

        filename = self.recv_data()
        self.logger.info(f"Recived filename: {filename}")

        savepath = self.recv_data()
        self.logger.info(f"END save path: {savepath}")

        savefile = os.path.join(savepath, filename)

        self.recv_file(savefile, bufsize)

        self.logger.info(f"END reciving file: {filename}, saved to: {savefile}")


import socket
import logging

class SocketStream:
    def __init__(self, host: str, port: int, 
                 is_server: bool = False,
                 base_logger: logging.Logger = None):
        self.host = host
        self.port = port
        self.is_server = is_server
        self.instance = "Server" if is_server else "Client"

        self.logging_config(base_logger)
        self.socket_config()

    def logging_config(self, base_logger: logging.Logger = None):
        logger_name = self.__class__.__qualname__
        if base_logger is None:
            self.logger = logging.getLogger(logger_name)
        else:
            self.logger = base_logger.getChild(logger_name)
        self.logger.info("Starting server")

    def socket_config(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.info(f"{self.instance} started on {self.host}:{self.port}")

        if self.is_server:
            self.s.bind((self.host, self.port))
            self.logger.info(f"Listen {self.host}:{self.port}")

    def connect(self):
        self.s.connect((self.host, self.port))

    def listen(self):
        self.s.listen(1)
        self.logger.info(f"Listen {self.host}:{self.port}")

    def accept(self):
        self.conn, self.addr = self.s.accept()
        self.logger.info(f"Client connected {self.addr}")

    def close_conn(self):
        self.conn.close()
        self.logger.info(f"Conection {self.addr} closed")

    def close(self):
        self.s.close()
        self.logger.info(f"{self.instance} stopped")

    def send(self, data: str):
        conn = self.conn if self.is_server else self.s
        conn.send(bytes(data, encoding="utf-8"))
        self.logger.info(f"Sended: {data}")
    
    def sendb(self, data: bytes):
        conn = self.conn if self.is_server else self.s
        conn.send(data)
        self.logger.info(f"Sended: {data}")

    def recv(self, bufsize: int) -> str:
        conn = self.conn if self.is_server else self.s
        data = conn.recv(bufsize).decode()
        self.logger.info(f"Recived: {data}")
        return data

    def recvb(self, bufsize: int) -> bytes:
        conn = self.conn if self.is_server else self.s
        data = conn.recv(bufsize)
        self.logger.info(f"Recived: {data}")
        return data

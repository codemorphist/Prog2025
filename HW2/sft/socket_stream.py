import socket
import logging
import io


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

        if self.is_server:
            self.listen()

    def logging_config(self, base_logger: logging.Logger = None):
        logger_name = self.__class__.__qualname__
        if base_logger is None:
            self.logger = logging.getLogger(logger_name)
        else:
            self.logger = base_logger.getChild(logger_name)
        self.logger.info(f"Starting {self.instance}")

    def socket_config(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if self.is_server:
            self.s.bind((self.host, self.port))
            self.logger.info(f"Binded {self.instance} to {self.host}:{self.port}")

        self.logger.info(f"{self.instance} started on {self.host}:{self.port}")

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

    def sendb(self, data: bytes):
        conn = self.conn if self.is_server else self.s
        conn.send(data)
        self.logger.info(f"Sended: {data}")

    def send(self, data: str):
        self.sendb(bytes(data, encoding="utf-8"))

    def send_datab(self, data: bytes):
        """
        Framing data:
            -> SIZE DATA_SIZE (HEADER)
            -> DATA
        """
        self.logger.info(f"BEGIN sending data: {data}")
        header = f"SIZE {len(data)}"
        self.send(header.ljust(32)) # 16 bytes header 
        self.sendb(data)
        self.logger.info("END sending data")

    def send_data(self, data: str):
        self.send_datab(bytes(data, encoding="utf-8"))

    def recvb(self, bufsize: int) -> bytes:
        conn = self.conn if self.is_server else self.s

        data = conn.recv(bufsize)
        self.logger.info(f"Recived: {data}")

        return data
    
    def recv(self, bufsize: int) -> str:
        return self.recvb(bufsize).decode()

    def recv_datab(self) -> bytes:
        """
        Unframing data:
            <- HEADER (SIZE DATA_SIZE)
            <- DATA 
        """
        self.logger.info(f"BEGIN reciving data")

        header = self.recv(32).strip()
        self.logger.info(f"Header: {header}")

        size = int(header.split()[1])
        self.logger.info(f"Bytes to recive: {size}")

        data = bytes()
        while size:
            data += self.recvb(1)
            size -= 1
        self.logger.info(f"END reciving data, recived: {data}")

        return data

    def recv_data(self) -> str:
        return self.recv_datab().decode()
        

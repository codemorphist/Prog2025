import logging
import socket 
from datetime import datetime


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def convert_date(date: str) -> str:
    formats = ["%d.%m.%Y", "%Y-%m-%d", "%m/%Y/%d"] 
    out_format = "%d.%m.%Y"

    for format in formats:
        try:
            return datetime.strptime(date, format).strftime(out_format)
        except ValueError:
            pass

    return ""


HOST = "localhost"
PORT = 8888
BUFSIZE = 10
MAX_CONNECTIONS = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info("Server was started")
s.bind((HOST, PORT))
s.listen(MAX_CONNECTIONS)

while True:
    conn, addr = s.accept()
    
    logger.info(f"Client {addr} connected")

    while True:
        data_bytes = conn.recv(BUFSIZE).strip()
        data = data_bytes.decode()
        logger.info(f"Reviced: {data} from client: {addr}")

        if data == "CLOSE":
            logging.info(f"Client {addr} disconected")
            conn.close()
            s.close()
            exit(0)

        converted = convert_date(data)
        conn.send(bytes(converted, encoding="utf-8").ljust(BUFSIZE))



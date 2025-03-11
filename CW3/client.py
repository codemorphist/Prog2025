import os
import sys
import socket
import time

from packet_stream import send_data, recv_data
from packet_stream import send_file, recv_file
from packet_stream import encode

from enum import Enum

class ClientType(str, Enum):
    BACKUP_SENDER = "Backup sender"
    BACKUP_RECVER = "Backup reciver"


class Client:
    def __init__(self, host: str, port: int, 
                 client_type: ClientType):
        self.host = host
        self.port = port
        self.client_type = client_type
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect()

    def connect(self):
        self.s.connect((self.host, self.port))

        while True:
            status = recv_data(self.s)
            if status == b"READY":
                return
            else:
                print("WAITING")
        
    def close(self):
        self.s.close()

    def backup(self):
        while True:
            if self.client_type is ClientType.BACKUP_SENDER:
                send_data(self.s, b"HELLO")
                time.sleep(1)
            else:
                print(recv_data(self.s).decode())

    def _send_backup(self, path: str):
        for dir, subdir, files in os.walk(path):
            send_data(self.s, encode(f"{dir} {subdir} {files}"))

    def _recv_backup(self, path: str):
        while data := recv_data(self.s):
            print(data)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999 

    t = sys.argv[1]
    if t == "sender":
        ct = ClientType.BACKUP_SENDER
    elif t == "recver":
        ct = ClientType.BACKUP_RECVER
    else:
        raise Exception("Invalid type of client")

    client = Client(HOST, PORT, ct)
    client.backup()
    client.close()

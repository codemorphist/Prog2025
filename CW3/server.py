import logging 

logging.basicConfig(level=logging.INFO,
                    format="[%(level)s] :: %(asctime)s : %(message)s")
logger = logging.getLogger(__name__)

import socketserver
from packet_stream import send_data, recv_data
from packet_stream import encode


class BackupServer(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        try:
            self.clients.append(self.request)
        except:
            self.clients = [self.request]
        print(f"CLIENT: {self.request} connected")

        if len(self.clients) == 2:
            for c in self.clients:
                send_data(c, b"READY")
            self.start_backup()
        else:
            send_data(self.clients[0], b"WAIT")

    def start_backup(self):
        sender, reciver = self.clients
        while True:
            data = recv_data(sender)
            send_data(reciver, data)
            

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), BackupServer) as server:
        print("SERVER STARTED")
        server.serve_forever()

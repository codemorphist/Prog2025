from packet_stream import PacketStream, recv_data


class Server(PacketStream):
    def __init__(self, host: str, port: int):
        super().__init__()

        self.host = host
        self.port = port
        self._socket.bind((host, port))

    def listen(self, backlog: int):
        self._socket.listen(backlog)

    def accept(self):
        return self._socket.accept()

    def close(self):
        self._socket.close()


if __name__ == "__main__":
    from config import HOST, PORT

    server = Server(HOST, PORT) 
    server.listen(1)
    conn, addr = server.accept()
    print("Client connected")
    while True:
        data = recv_data(server).decode()
        if data == "close":
            break
        print(data)
    conn.close()
    server.close()

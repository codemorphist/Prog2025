from packet_stream import PacketStream, send_data


class Client(PacketStream):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def connect(self):
        self._socket.connect((self.host, self.port))

    def close(self):
        self._socket.close()


if __name__ == "__main__":
    from config import HOST, PORT

    client = Client(HOST, PORT)
    client.connect()
        
    while True:
        data = bytes(input("> "), encoding="utf-8")
        send_data(client, data)
        if data == b"close":
            break

    client.close()


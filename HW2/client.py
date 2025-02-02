from packet_stream import PacketStream, send_data


class Client(PacketStream):
    def __init__(self):
        super().__init__()

    def connect(self, host: str, port: int):
        self._socket.connect((host, port))

    def close(self):
        self._socket.close()


if __name__ == "__main__":
    from config import HOST, PORT

    client = Client()
    client.connect(HOST, PORT)
        
    while True:
        data = bytes(input("> "), encoding="utf-8")
        send_data(client, data)
        if data == b"close":
            break

    client.close()


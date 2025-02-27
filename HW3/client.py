import socket
from config import HOST, PORT


class Client():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((HOST, PORT))

    def send_message(self, message):
        self.server.send(message.encode())

    def recv_message(self):
        return self.server.recv(2048).decode()

    def close(self):
        self.server.close()


if __name__ == "__main__":
    client = Client()
    gretting = client.recv_message()
    second = gretting == "You second"
    if second:
        print(client.recv_message())
    while True:
        message = input("> ")
        if message == "exit":
            break
        client.send_message(message)
        print(client.recv_message())
    client.close()

        

import socket
from config import HOST, PORT



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(100)


clients = []

while True:
    conn, addr = server.accept()
    print(f'[CLIENT] Connected from: {addr[0]}:{addr[1]}')
    clients.append((conn, addr))

    if len(clients) != 2:
        continue

    alise, bob = clients
    alise[0].send(b"You first")
    bob[0].send(b"You second")
    while True:
        m = alise[0].recv(2048)
        bob[0].send(bytes(f"[ALISE] {m}", encoding="utf-8"))
        
        m = bob[0].recv(2048)
        alise[0].send(bytes(f"[BOB] {m}", encoding="utf-8"))

conn.close()
server.close()

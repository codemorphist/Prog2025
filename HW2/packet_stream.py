import socket
import os
from collections import namedtuple
from io import BytesIO
import struct
from typing import Iterator


Header = namedtuple("Header", "size parts")
Packet = namedtuple("Packet", "size part data")

# Q: unsigned long long - Total file size to send
# Q: unsigned long long - Parts to send
HEADER_FMT = ">QQ"
HEADER_SIZE = struct.calcsize(HEADER_FMT)

# Q: unsigend long long - Size of part
# Q: unsigend long long - Current part
# {PACKET_DATA_SIZE}s - Data to send
PACKET_DATA_SIZE = 1024
PACKET_FMT = f">QQ{PACKET_DATA_SIZE}s"
PACKET_SIZE = struct.calcsize(PACKET_FMT)


def pack_header(header: Header) -> bytes:
    return struct.pack(HEADER_FMT, *header)


def unpack_header(packed_header: bytes) -> Header:
    return Header._make(struct.unpack(HEADER_FMT, packed_header))


def pack_packet(packet: Packet):
    return struct.pack(PACKET_FMT, *packet)


def unpack_packet(packed_packet: bytes) -> Packet:
    packet = Packet._make(struct.unpack(PACKET_FMT, packed_packet))
    data = packet.data.rstrip(b"\x00")
    return Packet(packet.size, packet.part, data)


def get_header(data: bytes) -> Header:
    data_size = len(data)
    parts = data_size // PACKET_DATA_SIZE

    if data_size < PACKET_DATA_SIZE:
        parts += 1

    header = Header(data_size, parts)
    return header


def get_packets(data: bytes) -> Iterator[Packet]:
    part = 0
    with BytesIO(data) as data_io:
        while packet_data := data_io.read(PACKET_DATA_SIZE):
            packet_size = len(packet_data)
            packet = Packet(packet_size, part, packet_data)
            part += 1
            yield packet


def send_data(socket: socket.socket, data: bytes):
    # send header
    h = get_header(data)
    header = pack_header(get_header(data))  
    socket.send(header)

    # send packets
    for packet in get_packets(data):
        socket.send(pack_packet(packet))


def recv_data(socket: socket.socket) -> bytes:
    # recv header
    header = unpack_header(socket.recv(HEADER_SIZE))

    # recv packets
    data = bytes()
    for _ in range(header.parts):
        recv_packet = socket.recv(PACKET_SIZE)
        packet = unpack_packet(recv_packet)
        data += packet.data

    return data


def encode(string: str) -> bytes:
    return bytes(string, encoding="utf-8")


def send_file(socket: socket.socket, 
              filepath: str, savepath: str):
    send_data(socket, b"INIT_FILE_TRANSFER")

    if recv_data(socket) != b"READY":
        return

    send_data(socket, encode(f"SAVE_TO {savepath}"))
    with open(filepath, "rb") as f:
        parts = os.stat(filepath).st_size // PACKET_DATA_SIZE
        for _ in range(parts): 
            data = f.read(PACKET_DATA_SIZE)
            send_data(socket, data)
    send_data(socket, b"EOF")


def recv_file(socket: socket.socket):
    data = recv_data(socket)
    if data != b"INIT_FILE_TRANSFER":
        return 
    send_data(socket, b"READY")

    data = recv_data(socket).decode().split()
    savepath = data[1]

    with open(savepath, "wb") as f:
        while True:
            data = recv_data(socket)
            if data == b"EOF":
                break
            f.write(data)


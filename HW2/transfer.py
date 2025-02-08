import socket
from packet_stream import encode
from packet_stream import send_file, recv_file
from packet_stream import send_data, recv_data
import argparse
import os


parser = argparse.ArgumentParser(prog="transfer.py",
                                 description="Simple CLI app to send and recive"
                                             "files or data by sockets")

parser.add_argument("conn_type", 
                    type=str,
                    choices=["server", "client"],
                    help="Type of connection")
parser.add_argument("conn_info", 
                    type=str,
                    help="Connection info")
parser.add_argument("op_type", 
                    type=str,
                    choices=["send", "recv"],
                    help="Operation type")
parser.add_argument("data_type", 
                    type=str,
                    choices=["file", "text"],
                    help="Data type")
parser.add_argument("data", 
                    nargs="?",
                    help="Data to send: path to file or text to send")
parser.add_argument("savepath",
                    nargs="?",
                    help="Path to save sended file")


def create_socket(conn_type: str, 
                  host: str, port: int) -> tuple:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    match conn_type:
        case "server":
            s.bind((host, port))
            print("-- SERVER started")
            s.listen(1)
            conn, addr = s.accept()
            print(f"-- CLIENT ({addr[0]}:{addr[1]}) connected")
            return conn, s
        case "client":
            print("-- CLIENT started")
            s.connect((host, port))
            print(f"-- Connected to SERVER ({host}:{port})")
            return s, None
        case _:
            raise ValueError(f"Invalid connection type: {conn_type}")


def transfer_file(s: socket.socket,
                  op_type: str, 
                  filepath: str, savepath: str):
    match op_type:
        case "send":
            print(f"-- START TRANFER FILE: {filepath}")
            print(f"-- FILE SIZE: {os.stat(filepath).st_size}")
            send_file(s, filepath, savepath)
        case "recv":
            print("-- START RECIVING FILE")
            path = recv_file(s)
            print(f"-- RECIVED FILE: {path}")
            print(f"-- RECIVED FILE SIZE: {os.stat(path).st_size}")


def transfer_data(s: socket.socket,
                  op_type: str, 
                  data: str):
    match op_type:
        case "send":
            print(f"-- START SENDING DATA: {data}")
            send_data(s, encode(data))
        case "recv":
            data = recv_data(s).decode()
            print(f"-- RECIVED: `{data}`")


def main():
    args = parser.parse_args()
    
    try: 
        host, port = args.conn_info.split(":")
    except:
        raise argparse.ArgumentTypeError("Invalid format of connection info. Use: HOST:PORT")

    try:
        port = int(port)
    except:
        raise ValueError("PORT must be integer")

    if port < 1025 or port > 65535:
        raise ValueError("PORT must be between 1025 and 65535")

    conn, s = create_socket(args.conn_type, host, port)

    match args.data_type:
        case "file":
            transfer_file(conn, args.op_type, args.data, args.savepath)
        case "text":
            transfer_data(conn, args.op_type, args.data)
        
    conn.close()
    if args.conn_type == "server":
        s.close()
    print("-- END CONNECTION")
    

if __name__ == "__main__":
    main()


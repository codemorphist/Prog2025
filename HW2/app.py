import sys
import tkinter as tk
from sft import FileTransferClient, FileTransferServer 

def main(instance: str,
         host: str, port: int):

    if instance == "client":
        instance_cls = FileTransferClient 
    else:
        instance_cls = FileTransferServer

    ft = instance_cls(host, port)
    
    print("Starting..")
    print("Strarting sync...")
    ft.sync()
    print("Connected")
    while True:
        command = input("> ")
        cmd, *args = command.split()

        match(cmd):
            case "send_file":
                ft.send_file_as(args[0], args[1])  
                print("File sended")
            case "recv_file":
                ft.recv_file_as()
                print("File revived")
            case "help":
                print("Avilable commands:\n"
                      "send_file <filepath> <savepath>\n"
                      "recv_file\n",
                      "exit\n")
            case "exit":
                ft.kill()
                exit()
            case _:
                print("Invalid command, try help")


HELP = """
Usage: 
    python app.py [client|server] [host]:[port]

Example:
    To run as server:
        python app.py server localhost:8888
    To connect as client:
        python app.py client localhost:8888
"""

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print(HELP)
        exit()

    if len(sys.argv) < 3:
        raise ValueError("Invalid count of arguments")

    instance = sys.argv[1].lower() # get instance type
    host, port = sys.argv[2].split(":")

    if instance not in ["client", "server"]:
        raise ValueError(f"Invalid instance type: {instance} {HELP}")

    main(instance, host, int(port))


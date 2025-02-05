import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SHOST = "localhost"
SPORT = 8888
BUFSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SHOST, SPORT))
logging.info(f"Connected to server {SHOST}:{SPORT}")

inputfile = input("Input file with dates: ")
outfile = input("Input file to output: ")

with open(inputfile, "r", encoding="utf-8") as f:
    logger.info("Starting reading file")

    out = open(outfile, "w")
    for line in f.readlines():
        date = line.replace("\n", "").strip()

        if not date:
            continue

        s.send(bytes(date, encoding="utf-8"))        
        logger.info(f"Sended to server: {date}")

        converted = s.recv(BUFSIZE).strip().decode()
        if converted:
            logger.info(f"Converted: {date} -> {converted}")
            out.write(f"{converted}\n")
        else:
            logger.warning("Empty bytes from server")

    out.close()
    logger.info("Ended reading file")

s.send(b"CLOSE".ljust(BUFSIZE))
s.close()
logger.info("Disconected from server")


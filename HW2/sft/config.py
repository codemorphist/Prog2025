from enum import Enum, auto

HOST = "localhost"
PORT = 8888

BUF_SIZE = 1024

class State(str, Enum):
    START_TRANSFER = auto()
    END_TRANSFER = auto()

LOGGING_FORMAT = "[%(levelname)s] %(asctime)s (%(name)s): %(message)s"
    


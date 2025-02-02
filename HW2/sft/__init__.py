from .server import FileTransferServer
from .client import FileTransferClient

from typing import TypeAlias

FileTransferInstance: TypeAlias = FileTransferClient | FileTransferServer



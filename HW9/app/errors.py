"""
This file contains error responce from server
"""

from app.responce import Responce, HTMLResponce
from app.http import StatusCode

from app.settings import DEBUG


def responce_400(error: str = "") -> Responce:
    return HTMLResponce("400.html", 
                         status=StatusCode.S400,
                         context={"error": error})


def responce_404(path: str = "") -> Responce:
    return HTMLResponce("404.html", 
                         status=StatusCode.S404,
                         context={"path": path})


def responce_500(error: str = "") -> Responce:
    if not DEBUG: # If not DEBUG don't show error info
        error = ""
    return HTMLResponce(
            "500.html", 
            status=StatusCode.S500,
            context={"error": error})


import os

from app.settings import STATIC_DIR, STATIC_PATH
from app.responce import Responce, HttpResponce
from app.errors import responce_404


def is_static(path: str) -> bool:
    path = path.lstrip("/").strip("/")
    return path.startswith(STATIC_DIR)


def static(path: str) -> Responce:
    path = path.lstrip("/").strip("/")
    file = path.split("static/")[1]
    if file == "":
        return responce_404()

    file_path = os.path.join(STATIC_PATH, file)
    _, ext = os.path.splitext(file_path)
    data = None

    try:
        with open(file_path, "r") as f:
            data = f.read()
    except:
        return responce_404()

    match ext:
        case ".css":
            mediatype = "text/css"
        case ".js":
            mediatype = "text/javascript"
        case _:
            mediatype = "text/plain"

    return Responce(data, headers=[("Content-Type", f"{mediatype}")])

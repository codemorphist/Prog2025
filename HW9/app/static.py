import os

from app.settings import STATIC_DIR, STATIC_PATH
from app.responce import Responce
from app.errors import responce_404
from app.templates import jinja_env


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


def staticpath(filepath: str):
    path = os.path.join(STATIC_PATH, filepath)
    if not os.path.exists(path):
        raise FileExistsError(f"Static file '{filepath}' not exists")

    return f"/static/{filepath}"

jinja_env.globals.update(staticpath=staticpath)

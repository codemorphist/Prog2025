import api

# List with url patterns
urlpatterns = [
    ("", api.index),
    ("add/", api.add),
    ("view/", api.view)
]


def normalize(path: str) -> str: 
    return path.strip("/")


def compare_pattern(path: str, pattern: str) -> bool:
    path_norm = normalize(path)
    pattern_norm = normalize(pattern)

    return path_norm == pattern_norm

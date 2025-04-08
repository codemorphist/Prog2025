"""
This file contains url routes for site

All routes must placed in urlpatters array in next format:
    (route, view function)
"""


import app.views as views

# List with url patterns
urlpatterns = [
    ("", views.index),
    ("add/", views.add),
    ("view/", views.view),

    ("api/get-toys/", views.get_toys)
]


def normalize(path: str) -> str: 
    return path.strip("/")


def compare_pattern(path: str, pattern: str) -> bool:
    path_norm = normalize(path)
    pattern_norm = normalize(pattern)

    return path_norm == pattern_norm

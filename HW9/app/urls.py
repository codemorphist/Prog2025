"""
This file contains url routes for site

All routes must placed in urlpatters array in next format:
    (route, view function)
"""


import app.views as views
from app.utils import path


# List with url patterns
urlpatterns = [
    path("", views.index, name="index"),
]




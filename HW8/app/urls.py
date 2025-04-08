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
    path("add-toy/", views.add_toy),
    path("delete-toy/<int:toy_id>/", views.delete_toy),
    path("view-toys/", views.view_toys),
    path("filter-toys/", views.filter_toys),
    path("api/get-toys/", views.get_toys),
]




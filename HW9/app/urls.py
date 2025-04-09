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
    path("add-student", views.add_student, name="add-student"),
    path("view-students", views.view_students, name="view-students"),
    path("student/<int:id>", views.view_student, name="view-student"),
    path("delete/<int:id>", views.delete_student, name="delete-student"),
    # path("edit/<int:id>", views.edit_student, name="edit-student"),
]




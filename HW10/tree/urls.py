from django.urls import path

import tree.views as views


app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),

    path('list/', views.TreeListView.as_view(), name='tree-list'),
    path('<int:pk>/', views.TreeView.as_view(), name='tree'),
    path('family/<int:pk>', views.TreeFamilyView.as_view(), name='family'),
    path('sort/<int:pk>', views.TreeSortView.as_view(), name='sort'),
    path('place/<int:pk>', views.PlaceView.as_view(), name='place'),

    path('add-tree/', views.TreeAddView.as_view(), name='add-tree'),
    path('add-family/', views.TreeFamilyAddView.as_view(), name='add-treefamily'),
    path('add-sort/', views.TreeSortAddView.as_view(), name='add-treesort'),
    path('add-place/', views.PlaceAddView.as_view(), name='add-place'),
    path('add-harvest/', views.HarverAddView.as_view(), name='add-harvest'),
]

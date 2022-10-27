from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.category_list, name="categories"),
    path("categories/<int:pk>/", views.category_detail, name="category_detail"),
    path("sub-categories/", views.sub_category_list, name="categories"),
    path(
        "sub-categories/<int:pk>/",
        views.sub_category_detail,
        name="sub_category_detail",
    ),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home, name="home"),
    path("test/", views.hello_world, name="homes"),
    path("products/", views.product_list, name="products"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("categories/", views.category_list, name="categories"),
    path("categories/<int:pk>/", views.category_detail, name="category_detail"),
    path(
        "categories/<int:pk>/products/<int:product_pk>/",
        views.product_in_category,
        name="category_detail",
    ),
    path("sub-categories/", views.sub_category_list, name="categories"),
    path(
        "sub-categories/<int:pk>/",
        views.sub_category_detail,
        name="sub_category_detail",
    ),
]

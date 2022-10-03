from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name="home"),
    path('test/', views.hello_world, name="homes"),
    path('products/', views.product_list, name="products"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
    path('categories/', views.category_list, name="categories"),
    path('category/<int:pk>/', views.category_detail, name="category_detail"),
    path('category/<int:pk>/product/<int:product_pk>/', views.product_in_category, name="category_detail"),
    path('sub-categories/', views.sub_category_list, name="categories"),
    path('sub-category/<int:pk>/', views.sub_category_detail, name="sub_category_detail"),
]



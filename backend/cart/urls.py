from django.urls import path
from . import views

urlpatterns = [
    path("carts/", views.cart_list, name="carts"),
    path("carts/<int:pk>/", views.cart_detail, name="cart_detail"),
    path("carts/<int:pk>/checkout/", views.cart_checkout, name="checkout")
]
from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.order_list, name="order_list"),
    path("orders/<int:pk>/", views.order_detail, name="order_detail"),
    path(
        "orders/customer/int:customer_pk>/", views.customer_order, name="customer_order"
    ),
]

from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.customer_list, name="home"),
    path("customers/<int:pk>/", views.customer_detail, name="profile"),
]

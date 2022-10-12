from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.customer_list, name="home"),
    path("customers/<int:pk>/", views.customer_detail, name="profile"),
    path("login/", views.login, name="login"),
    path("check/", views.is_auth, name="auth"),
]

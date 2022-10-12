from django.urls import path
from . import views


urlpatterns = [
    path('/home', views.home, name="home"),
    path('', views.vendor_list, name="vendors"),
    path('<int:pk>/', views.vendor_detail, name="vendors_detail")
]

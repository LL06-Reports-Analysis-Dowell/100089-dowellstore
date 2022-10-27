from django.urls import path
from . import views


urlpatterns = [
    path("vendors/", views.vendor_list, name="vendors"),
    path("vendors/<int:pk>/", views.vendor_detail, name="vendors_detail"),
]

from django.db import models


# Create your models here.


class Customer(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to="customer/")

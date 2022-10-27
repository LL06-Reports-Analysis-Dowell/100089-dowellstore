from django.db import models


# Create your models here.
class Customer(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100)
    name = models.CharField(null=False, max_length=100)
    phoneNumber = models.CharField(null=False, max_length=20)
    created = models.DateTimeField(auto_now=True)

    def register(self):
        self.save()

    @staticmethod
    def checkUser(email):
        try:
            return  Customer.objects.filter(email=email)
        except:
            return False

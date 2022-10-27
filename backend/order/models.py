from django.db import models

# Create your models here.
# Order Item
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save

    @staticmethod
    def customerOrders(customer_id):
        return Order.objects.filter(customer=customer_id).order_by("-date")
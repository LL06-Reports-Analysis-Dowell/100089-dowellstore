from django.db import models


#  PRODUCT CATEGORY

class ProductCategory(models.Model):
    name = models.TextField(null=False, max_length=225)
    code = models.IntegerField(null=False)
    description = models.CharField(null=False, max_length=500)
    parent_code = models.IntegerField(null=False)
    image = models.ImageField(null=True, upload_to='category/')

    def __str__(self):
        return self.name


# PRODUCT

class Product(models.Model):
    name = models.TextField(max_length=225)
    sku = models.CharField(max_length=225)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField(null=True, upload_to='product/')
    # category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Related Product
class RelatedProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    related_product_id = models.IntegerField(null=False)
    relevance_score = models.IntegerField(null=False)


# PRODUCT HISTORY

class PricingHistory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()


# PRODUCT VENDOR

class ProductVendor(models.Model):
    company_code = models.CharField(null=False, max_length=225)
    name = models.TextField(null=False, max_length=100)
    description = models.CharField(null=False, max_length=500)
    address_street_no = models.CharField(null=False, max_length=225)
    address_street_alt = models.CharField(null=False, max_length=225)
    address_city = models.CharField(null=False, max_length=225)
    address_state = models.CharField(null=False, max_length=225)
    address_postal_code = models.CharField(null=False, max_length=225)
    address_country_code = models.CharField(null=False, max_length=225)

    def __str__(self):
        return self.name

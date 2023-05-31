from django.db import models


class Tax(models.Model):
    percent = models.IntegerField()
    description = models.CharField(max_length=50, null=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    fast_code = models.IntegerField(null=True)
    base_price = models.FloatField()
    created_date = models.DateTimeField()
    tax_category = models.ForeignKey(Tax, on_delete=models.CASCADE)


class PriceCategory(models.Model):
    name = models.CharField(max_length=12)
    description = models.CharField(max_length=200, null=True)


class ProductPriceCategory(models.Model):
    price_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()

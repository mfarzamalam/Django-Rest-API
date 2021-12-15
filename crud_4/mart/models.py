from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    name = models.CharField(max_length=100)


class ShoppingCartItem(models.Model):
    name = models.CharField(max_length=100)
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    
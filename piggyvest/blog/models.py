from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Catalogue(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=7)
    address = models.TextField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

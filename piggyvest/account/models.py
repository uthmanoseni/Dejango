from django.db import models
# from .models import MyModel

# Create a model named 'Product'
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(primary_key=True, max_length=100)
    def __str__(self):
        return self.id

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # Foreign Key definition

    def __str__(self):
        return self.title


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    
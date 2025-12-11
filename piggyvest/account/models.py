from django.db import models
from django.contrib.auth import get_user_model
# from .models import MyModel

Users = get_user_model()

def audio_upload_to(instance, filename):
    return f"tasks/audios/{instance.owner.id if instance.owner else 'anon'}/{filename}"

def file_upload_to(instance, filename):
    return f"tasks/files/{instance.owner.id if instance.owner else 'anon'}/{filename}"

class Task(models.Model):
    owner = models.ForeignKey(Users, related_name='tasks', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    audio = models.FileField(upload_to=audio_upload_to, null=True, blank=True)
    attachment = models.FileField(upload_to=file_upload_to, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.text[:50] or f"Task {self.pk}"

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
    
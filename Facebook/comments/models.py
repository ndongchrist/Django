from django.db import models

# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length= 50)
    
class Book(models.Model):
    title = models.CharField(max_length=20)
    pages = models.IntegerField()
    

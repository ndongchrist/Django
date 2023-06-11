from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=200)
    username = models.CharField(max_length= 50)
    time = models.DateField()
    
class Test(models.Model):
    number = models.IntegerField()

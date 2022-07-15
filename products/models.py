from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)



class Product(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    description=models.CharField(max_length=300)


from django.db import models

# Create your models here.
class labs(models.Model):
    Name= models.CharField(max_length=100)
    Address= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Contactno= models.CharField(max_length=100)
    Description= models.CharField(max_length=1000)
    
class services(models.Model):
    Labname= models.CharField(max_length=100)
    Servicename= models.CharField(max_length=100)
    Servicecode= models.CharField(max_length=100)
    Price= models.CharField(max_length=100)
    Description= models.CharField(max_length=1000)
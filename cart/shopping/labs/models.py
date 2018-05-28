from django.db import models

# Create your models here.
class labs(models.Model):
    Name= models.CharField(max_length=100)
    Address= models.CharField(max_length=100)
    Email= models.CharField(max_length=100)
    Telno= models.CharField(max_length=100)

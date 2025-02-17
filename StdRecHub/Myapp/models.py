from django.db import models

# Create your models here.
class Records(models.Model):

    name  = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    dob = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    

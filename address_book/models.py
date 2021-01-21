from django.db import models

# Create your models here.

class Address(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=120)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)

    def __str__(self):
        return self.name
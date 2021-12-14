from django.db import models
from drivers.models import Driver
# Create your models here.


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    model = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    plate_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

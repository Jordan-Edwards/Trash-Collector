from django.db import models
from datetime import datetime


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    weekly_pickup_day = models.DateField(null=True)
    onetime_pickup = models.DateField(blank=True, null=True)
    start_suspension = models.DateField(blank=True, null=True)
    end_suspension = models.DateField(blank=True, null=True)
    balance = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

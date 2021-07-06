from django.db import models


# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employee(models.Model):
    name = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    todays_customers = []

    def __str___(self):
        return self.name

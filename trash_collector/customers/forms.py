from django.forms import ModelForm
from .models import Customer


class NewServiceForm(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "address",
                  "zip_code",
                  "weekly_pickup_day"}


class OneTimePickup(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "address",
                  "zip_code",
                  "onetime_pickup"}


class AccountSuspension(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "address",
                  "zip_code",
                  "start_suspension",
                  "end_suspension"}
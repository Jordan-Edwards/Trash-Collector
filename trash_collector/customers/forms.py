from django.forms import ModelForm
from .models import Customer


class NewServiceForm(ModelForm):
    class Meta:
        model = Customer
        fields = {"name",
                  "address",
                  "zip_code",
                  "weekly_pickup_day"}

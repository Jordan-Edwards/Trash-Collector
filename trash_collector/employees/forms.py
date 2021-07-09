from django.apps import apps
from django.forms import ModelForm
from .models import Employee


class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = {"name",
                  "user",
                  "zip_code"}


class ConfirmCharge(ModelForm):
    class Meta:
        Customer = apps.get_model('customers.Customer')
        model = Customer
        fields = {"balance"}

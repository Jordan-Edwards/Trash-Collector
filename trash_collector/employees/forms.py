from django.forms import ModelForm
from .models import Employee


class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = {"name",
                  "user",
                  "zip_code"}

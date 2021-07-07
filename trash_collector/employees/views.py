from datetime import date

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .forms import NewEmployeeForm

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.
from .models import Employee


def registration(request):
    form = NewEmployeeForm()
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees:index'))
    context = {'form': form}
    return render(request, 'employees/registration.html', context)


def index(request):
    if not request.user.groups.filter(name="Employees").exists():
        return render(request, 'home.html')
    Customer = apps.get_model('customers.Customer')
    user = request.user
    try:
        employee = Employee.objects.get(user=user)
        zip_code = employee.zip_code
        today_num = date.today().weekday()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        today_day = days[today_num]
        today_date = date.today()
        customers = Customer.objects.filter(Q(zip_code=zip_code) | Q(weekly_pickup_day=today_num),
                                            Q(start_suspension=today_date) | Q(end_suspension=today_date),
                                            Q(onetime_pickup=today_date))
        context = {
            'customers': customers
        }
        return render(request, 'employees/index.html', context)
    except Employee.DoesNotExist:
        return HttpResponseRedirect(reverse('employees:registration'))

from calendar import calendar
from datetime import date, datetime

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
        customers = Customer.objects.filter(zip_code=zip_code, weekly_pickup_day=today_day)
        one_time_pickup = Customer.objects.filter(onetime_pickup=today_date, zip_code=zip_code)
        context = {
            'customers': customers, 'one_time_pickup': one_time_pickup
        }
        return render(request, 'employees/index.html', context)
    except Employee.DoesNotExist:
        return HttpResponseRedirect(reverse('employees:registration'))

def daily_view(request, does_pickup=None):
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    Customer = apps.get_model('customers.Customer')
    customers = Customer.objects.filter(zip_code=employee.zip_code)
    does_pickup = False
    create_route = [does_pickup == True]
    for Customer in customers:
        context = {
            'create_route': create_route
        }
    return render(request, 'employees/route.html', context)

def confirm_pickup(request, customer_id):
    if request.method == "POST":
        Customer = apps.get_model('customers.Customer')
        customer = Customer.objects.get(id=customer_id)
        customer.balance += 5
        customer.save()
        return HttpResponseRedirect(reverse('employee:index'))
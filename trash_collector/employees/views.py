from datetime import date, datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .forms import NewEmployeeForm, ConfirmCharge
from .models import Employee
# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


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


def daily_view(request):
    user = request.user
    Customer = apps.get_model('customers.Customer')
    employee = Employee.objects.get(user_id=user.id)
    Customer.objects.filter(zip_code=employee.zip_code)
    route = []
    try:
        employee = Employee.objects.get(user=user)
        zip_code = employee.zip_code
        today_num = date.today().weekday()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        today_day = days[today_num]
        today_date = date.today()
        customers = Customer.objects.filter(zip_code=zip_code, weekly_pickup_day=today_day)
        one_time_pickup = Customer.objects.filter(onetime_pickup=today_date, zip_code=zip_code)
        start_date = Customer.start_suspension
        end_date = Customer.end_suspension
        if today_date.__le__(start_date) and today_date.__ge__(end_date):
            route.append(Customer)
        context = {
            'customers': customers, 'one_time_pickup': one_time_pickup, 'route': route
        }
        return render(request, 'employees/route.html', context)
    except Employee.DoesNotExist:
        return HttpResponseRedirect(reverse('employees:registration'))


def confirm_pickup(request):
    Customer = apps.get_model('customers.Customer')
    form = ConfirmCharge()
    if request.method == 'POST':
        form = ConfirmCharge()
        if form.is_valid():
            Customer.balance.save()
            return HttpResponseRedirect(reverse('employees:route'))
    context = {'form': form}
    return render(request, 'employees/confirmation.html', context)

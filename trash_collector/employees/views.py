from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.urls import reverse
from datetime import date


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    Customer = apps.get_model('customers.Customer')
    user = request.uset
    all_customers = Customer.objects.all()
    try:
        logged_in_employee = Employees.objects.get(user=user)
    except:
        return HttpResponseRedirect(reverse('employees:create'))
    context = {
        'logged_in_employee': logged_in_employee,
        'all_customers': all_customers,
    }
    return render(request, 'employees/index.html', context)


def registration(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_user = Employee(user=user, name=name, zip_code=zip_code)
        new_user.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/registration.html')


# HEAD

def daily_view(request):
    user = request.user
    logged_in_employee = Employees.objects.get(user=user)
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    curr_date = date.today()
    weekday = curr_date.strftime('%A')
    my_customers = []
    if request.method == "POST":
        for customer in all_customers:
            if customer.zip_code == logged_in_employee.zipcode and customer.pickup_day == weekday and customer.suspension_start == False or customer.onetime_pickup == weekday:
                my_customers.append(customer)
    return render(request, 'employees/filter.html')


def confirm_pickup(request, customer_id):
    if request.method == "POST":
        Customer = apps.get_model('customers.Customer')
        customer = Customer.objects.get(id=customer_id)
        customer.balance += 5
        customer.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/filter.html')

# END OF HEAD
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from .models import Employee
from django.urls import reverse
from datetime import date
from .forms import NewEmployeeForm
from customers.models import Customer
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'employees/index.html', context)


def registration(request):
    form = NewEmployeeForm()
    if request.method == 'POST':
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employees:index'))
    context = {'form': form}
    return render(request, 'employees/registration.html', context)


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
    return render(request, 'employees/Daily Route.html', context)


def confirm_pickup(request, customer_id):
    if request.method == "POST":
        Customer = apps.get_model('customers.Customer')
        customer = Customer.objects.get(id=customer_id)
        customer.balance += 5
        customer.save()
        return HttpResponseRedirect(reverse('employee:index'))
    else:
        return render(request, 'employees/filter.html')

# END OF HEAD

def filter(request, chosen_day):
    # chosen_day has value of "monday" or "tuesday", etc
    # use it to filter to find customers whose weekly day is equal to "chosen_day"
    # will also need a path in urls.py that allows for a string to be passed in
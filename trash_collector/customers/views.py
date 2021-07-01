from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_user = Customer(name=name,
                            address=address,
                            zip_code=zip_code,
                            weekly_pickup_day=weekly_pickup_day)
        new_user.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/register.html")

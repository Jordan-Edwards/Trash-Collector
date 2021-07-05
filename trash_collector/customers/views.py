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


# allows user to sign up for account
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


# create and edit trash pickup
def create_edit_pickup(request, user):
    if request.method == 'POST':
        if Customer.weekly_pickup_day == 'Null':
            weekly_pickup_day = request.POST.get('name')
            new_weekly_pickup_day = Customer(weekly_pickup_day=weekly_pickup_day)
            new_weekly_pickup_day.save()
            return HttpResponseRedirect(reverse('customers:index'))
        else:
            edit_weekly_pickup_day = Customer.objects.get(pk=user)
            context = {
                'edit_weekly_pickup_day': edit_weekly_pickup_day
            }
            if request.method == 'POST':
                edit_weekly_pickup_day.weekly_pickup_day = request.POST.get('weekly_pickup_day')
                edit_weekly_pickup_day.save()
                return HttpResponseRedirect(reverse('customers:index'))
            else:
                return render(request, "customers/edit_weekly_pickup.html", context)
    else:
        return render(request, "customers/home.html")


def onetime_pickup(request):
    if request.method == 'POST':
        onetime_pickup = request.POST.get('onetime_pickup')
        new_onetime_pickup = Customer(onetime_pickup=onetime_pickup)
        new_onetime_pickup.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, "customers/onetime_pickup.html")


def suspension(request):
    # if start_suspension == True:
    pass


def statement(request):
    pass


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
from .forms import NewEmployeeForm

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
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'employees/index.html', context)



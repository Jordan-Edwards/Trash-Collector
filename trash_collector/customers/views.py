from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewServiceForm, OneTimePickup, AccountSuspension
from .models import Customer


def index(request):
    user = request.user
    print(user)
    return render(request, 'customers/index.html')


# allows user to sign up for account
def registration(request):
    form = NewServiceForm()
    if request.method == 'POST':
        form = NewServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form}
    return render(request, "customers/registration.html", context)


def change(request, user_id):
    customer = Customer.objects.get(id=user_id)
    form = NewServiceForm(instance=customer)
    if request.method == 'POST':
        form = NewServiceForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/change.html', context)


def pickup(request, user_id):
    customer = Customer.objects.get(id=user_id)
    form = OneTimePickup(instance=customer)
    if request.method == 'POST':
        form = OneTimePickup(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/pickup.html', context)


def suspension(request, user_id):
    customer = Customer.objects.get(id=user_id)
    form = AccountSuspension(instance=customer)
    if request.method == 'POST':
        form = AccountSuspension(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:index'))
    context = {'form': form, 'customer': customer}
    return render(request, 'customers/suspension.html', context)


def statement(request, user_id):
    customer = Customer.objects.get(id=user_id)
    context = {
        'customer': customer
    }
    return render(request, 'customers/statement.html', context)

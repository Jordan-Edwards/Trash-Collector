from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewServiceForm

# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


# customer homepage


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
    return render(request, 'customers/registration.html', context)

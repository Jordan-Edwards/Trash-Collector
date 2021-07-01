from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('', views.registration, name="registration"),
    path('', views.create_edit_pickup, name="edit_weekly_pickup_day"),
    path('', views.onetime_pickup, name="onetime_pickup")
]

from django.urls import path

from . import views


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('', views.registration, name="registration"),
    path('', views.create_edit_pickup, name="edit_weekly_pickup_day"),
    path('', views.onetime_pickup, name="onetime_pickup"),
    path('', views.suspension, name="account_suspension"),
    path('', views.statement, name="statement")
]

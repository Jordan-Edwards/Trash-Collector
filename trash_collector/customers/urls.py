from django.urls import path
from . import views


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    # path('weekly_pickup/', views.edit_weekly_pickup_day, name="edit_weekly_pickup_day"),
    # path('onetime_pickup/', views.onetime_pickup, name="onetime_pickup"),
    # path('account_suspension/', views.suspension, name="account_suspension"),
    # path('statement/', views.statement, name="statement")
]

from django.urls import path
from . import views


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('change/<int:user_id>/', views.change, name="change"),
    # path('onetime_pickup/', views.onetime_pickup, name="onetime_pickup"),
    # path('account_suspension/', views.suspension, name="account_suspension"),
    # path('statement/', views.statement, name="statement")
]

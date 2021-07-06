from django.urls import path
from . import views


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('change/<int:user_id>/', views.change, name="change"),
    path('pickup/<int:user_id>/', views.pickup, name="pickup"),
    path('suspension/<int:user_id>/', views.suspension, name="suspension"),
    # path('statement/', views.statement, name="statement")
]

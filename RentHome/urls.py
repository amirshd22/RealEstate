from django.urls import path
from . import views

urlpatterns =[
    path('CreateRentHome/', views.CreateRentHome , name='CreateRentHome'),
    path('', views.HomeForRent , name='HomeForRent'),
    path('RentHomes/<int:Home_id>/', views.Homes_Details, name='Rent_Homes_Details'),

   

]
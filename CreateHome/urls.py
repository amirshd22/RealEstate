from django.urls import path
from . import views

urlpatterns =[
    path('CreateHome/', views.CreateHome , name='CreateHome'),
    path('HomeForSale/', views.HomeForSale , name='HomeForSale'),
    path('Homes<int:Home_id/>', views.Homes_Details, name='Homes_Details'),
]
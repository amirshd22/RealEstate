from django.urls import path
from . import views


urlpatterns =[
    
    path('BecomeAgent/', views.BecomeAgent, name='BCRES'),
    path('logout/', views.logout, name='logout'),
    path('loginAgent/', views.loginReal, name='loginreal'),


]
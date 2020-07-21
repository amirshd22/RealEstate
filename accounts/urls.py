from django.urls import path
from . import views


urlpatterns =[
    path('signUp/', views.signUp , name='signUp' ),
    path('login/', views.loginUser , name='login'),
    path('logout/', views.logout, name='logout'),
    path('BecomeRealEstate/', views.BecomeRealEstate, name='BCRES'),
    path('loginRealEstate/', views.loginReal, name='loginreal')

]
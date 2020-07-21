

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import random

# Create your views here.
def signUp(request):
    template='signUp.html'
    context = {}

    if request.method == 'POST':
        if request.POST['Password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.get(email=request.POST['Email'],)
                return render(request , template , {'error':'email address has already been used'})


            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['Email'] , email=request.POST['Email'], password=request.POST['Password'], first_name=request.POST['Firstname'], last_name=request.POST['Lastname'], is_active=False )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request , template , {'error':'Passwords must match'})

        

    else:

        return render(request , template , context)




#----------------------Become a Real Estate--------------------
def BecomeRealEstate(request):
    template='BCRES.html'
    context = {}

    if request.method == 'POST':
        if request.POST['Password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.get(email=request.POST['Email'],)
                return render(request , template , {'error':'email address has already been used'})


            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['Email'] , email=request.POST['Email'], password=request.POST['Password'], first_name=request.POST['Firstname'], last_name=request.POST['Lastname'], is_active=False )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request , template , {'error':'Passwords must match'})

        

    else:

        return render(request , template , context)





#-------------------for the user-----------------
def loginUser(request):
    template='login.html'
    context = {

    }
    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['Email'], password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request , template , {'error':'Email or password is incorrect'})
    else:
        return render(request , template , context)






#---------for the real estate---------------
def loginReal(request):
    template='loginreal.html'
    context = {

    }
    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['Email'], password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request , template , {'error':'Email or password is incorrect'})
    else:
        return render(request , template , context)







#--------------------logout the user-----------------------
def logout(request):
    template=''
    context = {}
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    

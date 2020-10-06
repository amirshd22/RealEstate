

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import forms

from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm


#----------------------Become agent--------------------
def BecomeAgent(request):
    form =  CreateUserForm()


    template='BCRES.html'

    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
       
    context = {'form' : form}
    return render(request , template , context)

#---------for the real estate---------------
def loginReal(request):
    template='loginreal.html'
    context = {

    }
    if request.method == 'POST':
        user = auth.authenticate(agent_username= request.POST['Email'], password=request.POST['Password'])
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
    

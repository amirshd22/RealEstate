

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import CreateUserForm


"""
    make a user with django forms 
"""
@unauthenticated_user
def BecomeAgent(request):
    template='BCRES.html'
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginreal')
        
        context = {'form': form}
        return render(request, template, context)

"""
    log the agent in 
"""
@unauthenticated_user
def loginReal(request):
    template= 'loginreal.html'
    context = {}
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['Email'], password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, template, {'error': 'Email or password is incorrect'})
    else:
        return render(request , template , context)

"""
    log the user out
"""
def logout(request):
    template=''
    context = {}
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')




from django.shortcuts import render



def home(request):
    templates= 'home.html'
    context={}
    return render(request , templates , context)
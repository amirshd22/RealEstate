from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required ,login_required2    
from .models import RentHome,PostImage 
from django.utils import timezone




#to CreateHome you should be logedin and also you should be a realesatate to logedin 
@login_required
def CreateRentHome(request):
    template = 'CreateRentHome.html'
    context={}
    if request.method == "POST":
        if request.POST['address'] and request.POST['title'] and request.POST['includes'] and request.POST['url'] and request.POST['Video_url'] and request.POST['price'] and request.POST['bath'] and request.POST['beds'] and request.POST['SQFT'] and request.FILES['img'] :
            rentHome = RentHome()
            rentHome.title = request.POST['title']
            rentHome.includes = request.POST['includes']
            #the url of the video that can be youtube or whatever
            if  request.POST['Video_url'].startswith('https://') or request.POST['url'].startswith('http://'):
                rentHome.video_url = request.POST['Video_url']
            else:
                rentHome.video_url = 'http://'+request.POST['Video_url']
            
            #the url of the website 
            if  request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):
                rentHome.website_url = request.POST['url']
            else:
                rentHome.website_url = 'http://'+request.POST['url']
            rentHome.sqft = request.POST['SQFT']
            rentHome.image = request.FILES['img']
            rentHome.beds = request.POST['beds']
            rentHome.bath = request.POST['bath']
            rentHome.price = request.POST['price']
            rentHome.address = request.POST['address']
            rentHome.date = timezone.datetime.now()
            rentHome.agent = request.user
            if request.POST['checkbox'] is not None :
                rentHome.newCo = True
            else:
                rentHome.newCo = False
            rentHome.save()
            return redirect('home')
        else:
            return render(request , template , {'error' : 'all Fields are required'})
    else:
        return render(request, template, context)





def HomeForRent(request):
    Homes = RentHome.objects.order_by('-date').all()
    template = 'RentHome.html'
    context ={
        'key1':Homes
    }

    return render(request , template , context)


def Homes_Details(request ,Home_id):
    template = 'RentHomeDetails.html'
    Homes= get_object_or_404(RentHome, pk=Home_id)
    context = {
        'key2':Homes
    }

    return render(request , template , context)

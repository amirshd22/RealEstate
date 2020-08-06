from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required ,login_required2    
from .models import SellHomes,PostImage 
from django.utils import timezone




#to CreateHome you should be logedin and also you should be a realesatate to logedin 
@login_required
def CreateHome(request):
    template = 'CreateHome.html'
    context={}
    if request.method == "POST":
        if request.POST['address'] and request.POST['title'] and request.POST['includes'] and request.POST['url'] and request.POST['Video_url'] and request.POST['price'] and request.POST['bath'] and request.POST['beds'] and request.POST['SQFT'] and request.FILES['img'] :
            sellHomes = SellHomes()
            sellHomes.title = request.POST['title']
            sellHomes.includes = request.POST['includes']
            #the url of the video that can be youtube or whatever
            if  request.POST['Video_url'].startswith('https://') or request.POST['url'].startswith('http://'):
                sellHomes.video_url = request.POST['Video_url']
            else:
                sellHomes.video_url = 'http://'+request.POST['Video_url']
            
            #the url of the website 
            if  request.POST['url'].startswith('https://') or request.POST['url'].startswith('http://'):
                sellHomes.website_url = request.POST['url']
            else:
                sellHomes.website_url = 'http://'+request.POST['url']
            sellHomes.sqft = request.POST['SQFT']
            sellHomes.image = request.FILES['img']
            sellHomes.beds = request.POST['beds']
            sellHomes.bath = request.POST['bath']
            sellHomes.price = request.POST['price']
            sellHomes.address = request.POST['address']
            sellHomes.date = timezone.datetime.now()
            sellHomes.agent = request.user
            if request.POST['checkbox'] is not None :
                sellHomes.newCo = True
            else:
                sellHomes.newCo = False
            sellHomes.save()
            return redirect('home')
        else:
            return render(request , template , {'error' : 'all Fields are required'})
    else:
        return render(request, template, context)





def HomeForSale(request):
    Homes = SellHomes.objects.all()
    template = 'SellHome.html'
    context ={
        'key':Homes
    }

    return render(request , template , context)


def Homes_Details(request ,Home_id):
    template = 'HomeDetails.html'
    Homes= get_object_or_404(SellHomes, pk=Home_id)
    context = {
        'key':Homes
    }

    return render(request , template , context)

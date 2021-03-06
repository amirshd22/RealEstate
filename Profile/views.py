from django.http import Http404
from django.shortcuts import render, redirect
from CreateHome.models import SellHomes
from RentHome.models import RentHome
from .forms import ProfileForm, ProfileBasicForm
from .models import Profile
from django.contrib.auth.decorators import login_required
def profile_update_view(request, *args, **kwargs):
    template = 'editprofile.html'
    if not request.user.is_authenticated: # is_authenticated()
        return redirect("login")
    user = request.user
    user_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
    my_profile = user.profile
    form = ProfileForm(request.POST or None, instance=my_profile, initial=user_data)
    if form.is_valid():
        profile_obj = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        profile_obj.save()
    context = {
        "form": form,
        "btn_label": "Save",
        "title": "Update Profile",
       
    }
    return render(request,template, context)


@login_required
def profile_detail_view(request, username,*args, **kwargs):
    # get the profile for the passed username
    template= "profile.html"
    user_sell_homes = SellHomes.objects.filter(agent__username= username).order_by('-date').all()
    user_rent_homes = RentHome.objects.filter(agent__username= username).order_by('-date').all()
    qs = Profile.objects.filter(user__username=username)
 
 
    profile_obj = qs.first()
    
    is_following = False
    if request.user.is_authenticated:
        user = request.user
        is_following = user in profile_obj.followers.all()
        # is_following = profile_obj in user.following.all()
    context = {
        "username": username,
        "profile": profile_obj,
        "is_following": is_following,
        'sell_homes':user_sell_homes,
        "rent_home":user_rent_homes,
     

     
     

    }
    return render(request, template, context)
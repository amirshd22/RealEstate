from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SellHomes(models.Model):
    title= models.CharField(max_length=300)#the title of the house 

    image=models.ImageField(blank=True)#the images of the house
    
    includes= models.TextField()#more infromation about the houese

    beds=models.IntegerField()#the number of beds
    
    bath=models.IntegerField()#the number of baths
   
    price = models.FloatField()#the price 
    
    sqft = models.FloatField()#the squaare feet for the meeetee

    newCo = models.BooleanField()#if it is new or not 

    date=models.DateField(auto_now=True)#the date of the realeees
    
    video_url = models.URLField()#this is for video 

    website_url = models.URLField()#the url of the agents person to import his/her own website

    agent = models.ForeignKey(User, on_delete=models.CASCADE)#the agent that is 

    address = models.TextField(null=True)

    def __str__(self):
        return self.title



class PostImage(models.Model):
    post = models.ForeignKey(SellHomes, default=None ,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')


from django.db import models

# Create your models here.
class Homes(models.Model):
    title= models.CharField(max_length=300)

    image=models.ImageField(blank=True)
    
    beds=models.IntegerField(blank=False, null=True)
    
    bath=models.IntegerField(blank=False, null=True)
   
    price = models.FloatField(blank=True, null=True)
    
    date=models.DateField(auto_now=True)
    
    


    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Homes, default=None ,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')


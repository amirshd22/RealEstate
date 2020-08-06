from django.contrib import admin

# Register your models here.
from .models import RentHome ,PostImage
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(RentHome)
class PostAdmin(admin.ModelAdmin):
    inlines =[PostImageAdmin]

    class Meta:
        model=RentHome

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
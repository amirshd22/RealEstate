from django.contrib import admin

# Register your models here.
from .models import Homes ,PostImage
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(Homes)
class PostAdmin(admin.ModelAdmin):
    inlines =[PostImageAdmin]

    class Meta:
        model=Homes

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
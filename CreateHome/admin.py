from django.contrib import admin

# Register your models here.
from .models import SellHomes ,PostImage
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(SellHomes)
class PostAdmin(admin.ModelAdmin):
    inlines =[PostImageAdmin]

    class Meta:
        model=SellHomes

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
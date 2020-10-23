
from django.contrib import admin 
from django.urls import path, include , re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/', include('accounts.urls')),
    path('', views.home , name='home'),
    path('HomesForSale/', include('CreateHome.urls')),
    path('HomesForRent/', include('RentHome.urls')),
    path('profiles/', include('Profile.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('inner',TemplateView.as_view(template_name='inner.html'), name='inner'),
    path('about',TemplateView.as_view(template_name='about.html'), name='about'),
    path('login',login_view, name='login'),
    path('logout',logout_view, name='logout'),
    path('register',register_view, name='register'),
    path('contact', contact_view, name='contact'),
    path('profile', profile_view, name='profile'),
    path('profile/update', profile_update_view, name='profile_update'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
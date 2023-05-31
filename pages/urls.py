from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contanct',views.contanct,name='contanct'),
    path('service',views.service,name='service'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
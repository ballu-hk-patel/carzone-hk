from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contanct',views.contanct,name='contanct'),
    path('service',views.service,name='service'),
]
from django.shortcuts import render
from pages.models import Team
from cars.models import car 

# Create your views here.
def home(request):
    ss=[]
    teams= Team.objects.all()
    featured_car=car.objects.order_by('-created_date').filter(is_featured=True)
    all_car=car.objects.order_by('-created_date')
    for i in all_car:
        if i.car_photo and i.car_photo_1 and i.car_photo_2 and i.car_photo_3 and i.car_photo_4 :
            ss.append(4)
        elif i.car_photo and i.car_photo_1 and i.car_photo_2 and i.car_photo_3:
            ss.append(3)
        else :
            ss.append(2)
    
    
    data={
        'teams': teams,
        'featured_car':featured_car,
        'all_car':all_car,
        'zipped_app_list': zip(all_car, ss)
        
    }
    return render(request, 'pages/home.html',data)

def about(request):
    teams= Team.objects.all()
    data={
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)

def contanct(request):
    return render(request, 'pages/contact.html')

def service(request):
    return render(request, 'pages/service.html')

# def cars(request):
#     return pass

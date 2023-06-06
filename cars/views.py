from django.shortcuts import render, get_object_or_404
from .models import car
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
# Create your views here.
def cars(request):
    cars=car.objects.order_by('-created_date')
    paginator=Paginator(cars,4)
    page= request.GET.get('page')
    paged_cars=paginator.get_page(page)

    model_search=car.objects.values_list('model',flat=True).distinct() # this get only unique value for showing in front page 
    city_search=car.objects.values_list('city',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    body_style=car.objects.values_list('body_style',flat=True).distinct()

    data={
        'cars':paged_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style':body_style,
    }
    return render(request, 'cars/cars.html',data)

def car_details(request,id):
    single_car= get_object_or_404(car, pk=id)
    data={"id":id,
       "single_car": single_car,}
    return render(request,'cars/car_details.html',data)

def search(request):
    cars=car.objects.order_by('-created_date')
    ss=""

    model_search=car.objects.values_list('model',flat=True).distinct() # this get only unique value for showing in front page 
    city_search=car.objects.values_list('city',flat=True).distinct()
    year_search=car.objects.values_list('year',flat=True).distinct()
    body_style=car.objects.values_list('body_style',flat=True).distinct()
    tra=car.objects.values_list('transmission',flat=True).distinct()
    # ss=request.GET.get('keyword') # get html tage name using fetching the data
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        print(keyword)

        if keyword:
            count1=cars.filter(car_title__icontains=keyword).count()
            if int(count1) == 0:
                ss=keyword+" is not Avilable ,At this time !"
            if  int(count1) != 0:
                print("priting...")
                cars=cars.filter(car_title__icontains=keyword)

    if 'model' in request.GET:
        model=request.GET['model']
        print(model)
        if model:
            cars=cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city=request.GET['city']
        print(city)
        if city:
            cars=cars.filter(city__iexact=city)


    if 'year' in request.GET:
        year=request.GET['year']
        print(year)
        if year:
            cars=cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style=request.GET['body_style']
        print(body_style)
        if body_style:
            cars=cars.filter(body_style__iexact=body_style)
       
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price,price__lte=max_price)

    if 'transmission' in request.GET:
        transmission=request.GET['transmission']
        if transmission:
            cars=cars.filter(transmission__icontains=transmission)


    data={
        'cars':cars,
        'ss':ss,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style':body_style,
        'tra':tra,
        
    }
    return render(request,'cars/search.html',data)
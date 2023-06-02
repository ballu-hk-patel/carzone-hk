from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
class carAdmin(admin.ModelAdmin):
    def thumbnail (self,object):
        return format_html('<img src={} width="40px" style="border-radius:50%;" />'.format(object.car_photo.url)) # car_photo comes from model attribute
    
    thumbnail.short_description ='car_photo'
    
    list_display=('id','thumbnail','car_title','color','model','year','price','body_style','engine','is_featured')
    list_display_links=('id','thumbnail','car_title')
    list_editable=('is_featured',)
    list_filter=('car_title',)
    search_fields=('car_title','model','body_style')


admin.site.register(car,carAdmin)
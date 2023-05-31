from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    fb_link = models.URLField(max_length=100)
    twi_link = models.URLField(max_length=100)
    goo_link = models.URLField(max_length=100)

    def __str__(self):
        return self.first_name


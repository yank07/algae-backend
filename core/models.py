from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
ROLE_CHOICES = [
        ('biologist', 'Biologist'),
        ('citizen', 'Citizen'),
    ]
class User(AbstractUser):
    location = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,null=True, blank=True, default='citizen')
##TODO change to Lat, Long. Add Zip Code, Country City, Address 1, Addres 2    

class Observation(models.Model):
#TODO creaate others values as PH, water clarity, temperture and other fields that might be relveante and pondarate them in algae level.
#TODO add lat, log. Possibly levels changes with the location in the same body of water. 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body_of_water = models.CharField(max_length=255)
    algae_level = models.FloatField()
    observation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

class Request(models.Model):
    biologist = models.ForeignKey(User, on_delete=models.CASCADE)
    body_of_water = models.CharField(max_length=255)
    request_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    is_fulfilled = models.BooleanField(default=False)

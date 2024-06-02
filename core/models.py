from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=255, blank=True, null=True)

class Observation(models.Model):
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

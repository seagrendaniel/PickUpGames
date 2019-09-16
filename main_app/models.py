from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    homecourt = models.CharField(max_length=50)


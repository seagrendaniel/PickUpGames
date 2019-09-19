from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Park(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    courts = models.IntegerField()
    schedule = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def games_planned(self):
            return self.game_set.all()

class Game(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    count = models.IntegerField()
    game = models.CharField(max_length=100)
    
    # def __str__(self):
    #     return self.park

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'game_id': self.id})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    homecourt = models.CharField(max_length=50)
    games = models.ManyToManyField(Game)
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for profile_id: {self.profile_id} @{self.url}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):   
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
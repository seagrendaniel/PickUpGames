from django.contrib import admin
from .models import Profile, Game, Park
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Park)
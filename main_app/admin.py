from django.contrib import admin

from .models import Profile, Game, Park, Photo

from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Game)

admin.site.register(Photo)

admin.site.register(Park)


from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, NewGameForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game, Photo, Park

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'pickupgames1'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def profile_show(request):
  return render(request, 'profile.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.profile.position = form.data['position']
      user.profile.height = form.data['height']
      user.profile.location = form.data['location']
      user.profile.homecourt = form.data['homecourt']
      login(request, user)
      return redirect('/profile/')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignupForm()
  context = {
    'form': form,
    'error_message': error_message
  }

  return render(request, 'registration/signup.html', context)

class ParkCreate(LoginRequiredMixin, CreateView):
  model = Park
  fields = ['name', 'address', 'zipcode', 'courts', 'schedule', 'lat', 'long']

class ParkDelete(LoginRequiredMixin, DeleteView):
  model = Park
  success_url = '/parks/'

@login_required
def parks_index(request):
  parks = Park.objects.all()
  print(parks)
  for park in parks:
    print('park name', park.name)
  return render(request, 'parks/index.html', {'parks': parks})

@login_required
def parks_detail(request, park_id):
  park = Park.objects.get(id=park_id)
  new_game_form = NewGameForm()
  return render(request, 'parks/detail.html', {'park': park, 'new_game_form': new_game_form})

@login_required
def add_game(request, park_id):
  form = NewGameForm(request.POST)
  if form.is_valid():
    new_game = form.save(commit=False)
    new_game.park_id = park_id
    print(new_game)
    new_game.save()
  return redirect('parks_detail', park_id = park_id)


class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['game', 'date', 'time']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['date', 'time']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

@login_required
def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)

  return render(request, 'games/detail.html', { 'game': game })

@login_required
def join_game(request, profile_id, game_id):
  Profile.objects.get(id=profile_id).games.add(game_id)
  return redirect('profile', profile_id=profile_id)

@login_required
def leave_game(request, profile_id, game_id):
  Profile.objects.get(id=profile_id).games.remove(game_id)
  return redirect('profile', profile_id=profile_id)

@login_required
def add_photo(request, profile_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"   
            # print(url)         
            photo = Photo(url=url, profile_id=profile_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('/profile/', profile_id=profile_id) 

class PhotoDelete(LoginRequiredMixin, DeleteView):
  model = Photo 
  success_url = '/profile/'

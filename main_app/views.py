from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import Game

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

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['location', 'date', 'time']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def mygames_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request, 'games/index.html', {'games': games})

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  game_doesnt_have = Game.objects.exclude(id__in = game.all().values_list('id'))
  return render(request, 'games/detail.html', {
    'game': game,
    'games': game_doesnt_have
  })
  

class GameList(LoginRequiredMixin, ListView):
  model = Game

class GameDetail(LoginRequiredMixin, DetailView):
  model = Game


class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


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
      # This is how we login in programatically
      login(request, user)
      return redirect('/profile/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request
  form = SignupForm()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'registration/signup.html', context)


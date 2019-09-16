from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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
  profile_form = ProfileForm()
  context = {
    'form': form,
    'profile_form': profile_form,
    'error_message': error_message
  }
  return render(request, 'registration/signup.html', context)


# @login_required
@transaction.atomic
def update_profile(request):
  if request.method == 'POST':
    user_form = SignupForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, _('Your profile was successfully updated!'))
      return redirect('/profile/')
    else: 
      messages.error(request, _('Please correct the errors below'))
  else: 
    user_form = SignupForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
  return render(request, 'profile.html', {
    'user_form': user_form,
    'profile_form': profile_form
  })  


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


positions = [
    ('point guard', 'Point Guard'),
    ('shooting guard', 'Shooting Guard'),
    ('small forward', 'Small Forward'),
    ('power forward', 'Power Forward'),
    ('center', 'Center')
]

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput (attrs={'placeholder':'Kobe'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput (attrs={'placeholder':'Bryant'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    position = forms.CharField(label='Position Played', required=True, widget=forms.Select (choices=positions))
    height = forms.CharField(max_length=10, required=True, widget=forms.TextInput (attrs={'placeholder':'6\'6'}))
    location = forms.CharField(max_length=50, required=True, widget=forms.TextInput (attrs={'placeholder':'Los Angeles'}))
    homecourt = forms.CharField(max_length=50, required=False, widget=forms.TextInput (attrs={'placeholder':'Staples Center'}))

    class Meta:
        model = Profile
        fields = ('position', 'height', 'location', 'homecourt')        
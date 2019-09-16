from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput (attrs={'placeholder':'Kobe'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput (attrs={'placeholder':'Bryant'}))
    # position = forms.ChoiceField('Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center', required=True, widget=forms.TextInput (attrs={'placeholder':'Shooting Guard'}))
    location = forms.CharField(max_length=50, required=True, widget=forms.TextInput (attrs={'placeholder':'Los Angeles'}))
    homecourt = forms.CharField(max_length=50, required=False, widget=forms.TextInput (attrs={'placeholder':'Staples Center'}))

    
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'location', 'homecourt', 'password1', 'password2']
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    fullname = forms.CharField(max_length = 30, required = True)
    email = forms.EmailField(max_length = 30, help_text = 'Required. Enter the Valid Email')

    class Meta:
        model = User
        fields = ['username','fullname','email','password1','password2']

class MovieForm(forms.Form):
    movie_name = forms.CharField(label = 'Enter movie name', max_length = 100)
    year = forms.CharField(label = 'Year')

class WishList(forms.Form):
    movie_name = forms.CharField(label = "Enter your movie_name", max_length = 100)

class WatchLater(forms.Form):
    movie_name = forms.CharField(label = 'Enter your movie_name', max_length = 100)
    
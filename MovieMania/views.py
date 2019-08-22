from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here
from .forms import MovieForm, WishList, WatchLater
from .forms import SignUpForm
import requests

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url = 'login')
def main(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data['movie_name']
            year = form.cleaned_data['year']  
            apikey = '767da9db'
            try:
                response = requests.get('http://www.omdbapi.com/?t=' + movie_name + '&apikey=' + apikey + '&y=' + year)
                data = response.json()
                return render(request, template_name = 'display.html', context = {
                'movie_name':data['Title'],
                'year':data['Year'],
                'poster':data['Poster'],
                'plot': data['Plot'],
                'imdbrating': data['imdbRating'],
                'genre': data['Genre'],
                'released':data['Released'],
                'votes': data['imdbVotes'],
                'runtime': data['Runtime'],
                'writer': data['Writer'],
                'language': data['Language'],
                'actors': data['Actors'],
                'country': data['Country'],
                'director': data['Director'],
            })
            except KeyError as ke:
                return render(request, template_name = 'keyerror.html')
    else:
        form = MovieForm()
        return render(request,template_name = 'main.html', context = {'form': form})
        
def wishlist(request):
    if request.method == 'POST':
        form = WishList(request.POST)
        return render(request, template_name = 'success.html')
    else:
        form = WishList()
        return render(request, template_name = 'wishlist.html', context={'form': form})

def watchlater(request):
    if request.method == 'POST':
        return render(request, template_name = 'success.html')
    else:
        form = WatchLater()
        return render(request, template_name = 'watchlater.html', context ={'form': form})

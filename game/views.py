from django.shortcuts import render
from django.views import generic

# Create your views here.
def home(request):
	return render(request, 'game/index.html')

def game(request):
	return render(request, 'game/game.html')

def scores(request):
	return render(request, 'game/scores.html')

def profile(request):
	return render(request, 'game/profile.html')


		
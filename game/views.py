from django.shortcuts import render
from django.views import generic

# Create your views here.
def game(request):
	return render(request, 'game/index.html')
		
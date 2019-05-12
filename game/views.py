from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Category

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'category_list'

    def get_queryset(self):
    	return Category.objects.all()

def game(request):
	category = request.POST['category']
	# print(category)
	return render(request, 'game/game.html', {'category': category})

def scores(request):
	return render(request, 'game/scores.html')

def profile(request):
	return render(request, 'game/profile.html')


		
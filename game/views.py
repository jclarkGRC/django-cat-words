from django.shortcuts import get_object_or_404, render
from django.views import generic
from game.models import Category, CurrentCategory

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'game/index.html'
    context_object_name = 'category_list'

    def get_queryset(self):
    	return Category.objects.all()

def game(request):
	if request.method == 'POST':
		if CurrentCategory.objects.get(id=1):
			current_category = CurrentCategory.objects.get(id=1)
			current_category.current_category_text = request.POST['category']
			current_category.save()
		return render(request, 'game/game.html', {'category': current_category.current_category_text})
	else:
		return render(request, 'game/game.html', {'category': "choose a category"})

def scores(request):
	return render(request, 'game/scores.html')

def profile(request):
	return render(request, 'game/profile.html')


		
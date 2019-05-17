from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from game.models import Category, CurrentCategory, CurrentWord

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'game/index.html'
#     context_object_name = 'category_list'

#     def get_queryset(self):
#     	return Category.objects.all()

def index(request):
	if request.method == 'POST':
		if CurrentCategory.objects.get(id=1):
			current_category = CurrentCategory.objects.get(id=1)
			current_category.current_category_text = request.POST['category']
			current_category.save()
			args = {'category': current_category.current_category_text}
		return redirect('play/', args)
	else:
		category_list = Category.objects.all()
		return render(request, 'game/index.html', {'category_list': category_list})

def game(request):
	if request.method == 'POST':
		obj = CurrentWord.objects.filter(id=1).first()
		if obj != None:
			current_word = CurrentWord.objects.get(id=1)
			current_word.current_word_text = request.POST['current_word']
			current_word.save()
			args = {'current_word': current_word}
			return render(request, 'game/game.html', args)
		else:
			#current_word = CurrentWord(current_word_text=request.POST['current_word_text'])
			#args = {'current_word': current_word}
			current_word_text = request.POST['current_word']
			current_word = CurrentWord(current_word_text=current_word_text);
			args = {'current_word': current_word.current_word_text}
			return render(request, 'game/game.html', args)
	else:
		if CurrentCategory.objects.get(id=1):
			current_category = CurrentCategory.objects.get(id=1)
			args = {'category': current_category.current_category_text}
			return render(request, 'game/game.html', args)

def scores(request):
	return render(request, 'game/scores.html')

def profile(request):
	return render(request, 'game/profile.html')


		
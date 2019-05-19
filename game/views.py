from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from game.models import Category, CurrentCategory, CurrentWord, SavedWord

def index(request):
	if request.method == 'POST':
		current_category = CurrentCategory.objects.get()
		current_category.current_category_text = request.POST['category']
		current_category.save()
		args = {'category': current_category.current_category_text}
		return redirect('play/', args)
	else:
		category_list = Category.objects.all()
		return render(request, 'game/index.html', {'category_list': category_list})

def game(request):
	if request.method == 'POST':
		current_category = CurrentCategory.objects.get()
		saved_words = SavedWord.objects.all()
		if CurrentWord.objects.get():
			current_word = CurrentWord.objects.get()
			current_word.current_word_text = request.POST['current_word']
			current_word.save()
		else:
			current_word = CurrentWord(current_word_text=request.POST['current_word'])
			current_word.save()
		saved_word = SavedWord(saved_word_text=request.POST['current_word'])
		saved_word.save()
		args = {
		'category': current_category.current_category_text, 
		'current_word': current_word.current_word_text, 
		'saved_words': saved_words,
		'letter_guess': current_word.current_word_text[-1].upper()
		}
		return render(request, 'game/game.html', args)
	if request.GET.get('clear_saved_words'):
		current_word = CurrentWord.objects.filter(pk=1)
		current_category = CurrentCategory.objects.get(id=1)
		SavedWord.objects.all().delete()
		args = {'category': current_category.current_category_text}
		return render(request, 'game/game.html', args)
	else:
		current_category = CurrentCategory.objects.get(id=1)
		return render(request, 'game/game.html', {'category': current_category.current_category_text})


def scores(request):
	return render(request, 'game/scores.html')

def profile(request):
	return render(request, 'game/profile.html')



		
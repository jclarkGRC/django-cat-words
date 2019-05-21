from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from game.models import Category, CurrentCategory, CurrentWord, SavedWord, CurrentScore

# index view
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

# game view
def game(request):
	if request.method == 'POST':
		current_category = CurrentCategory.objects.get()
		saved_words = SavedWord.objects.all()
		current_score = calculateScore(100)
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
		'letter_guess': current_word.current_word_text[-1].upper(),
		'current_score': current_score
		}
		return render(request, 'game/game.html', args)
	if request.GET.get('clear_saved_words'):
		current_word = CurrentWord.objects.filter(pk=1)
		current_category = CurrentCategory.objects.get(id=1)
		SavedWord.objects.all().delete()
		current_score = calculateScore(0)
		args = {
		'category': current_category.current_category_text,
		'current_score': current_score
		}
		return render(request, 'game/game.html', args)
	else:
		current_category = CurrentCategory.objects.get(id=1)
		return render(request, 'game/game.html', {'category': current_category.current_category_text})

# game view functions

# The calculateScore function calculates the users score during gameplay
# @params score  The amount at which the score will increase
def calculateScore(score):
	current_score = CurrentScore.objects.get()
	# If score is zero reset the score to zero
	if score == 0:
		current_score.current_score_text = 0
	# Add the score paramenter to the current score
	else:
		current_score.current_score_text = current_score.current_score_text + score
	# Save the current score to the database
	current_score.save()
	# Return the current score
	return current_score.current_score_text


# instructions view
def instructions(request):
	return render(request, 'game/instructions.html')

# scores view
def scores(request):
	return render(request, 'game/scores.html')
# profile view
def profile(request):
	return render(request, 'game/profile.html')



		
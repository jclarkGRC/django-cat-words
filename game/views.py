# views.py
# Created by Joshua Clark on 5/20/19

from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from game.models import Category, CurrentCategory, CurrentWord, SavedWord, CurrentScore

# THE INDEX VIEW


def index(request):
	# If a category was chosen, save the category and proceed to the game view
	if request.method == 'POST':
		# Save the current category to be used during gameplay
		current_category_text = saveCurrentCategory(request)
		# Arguments to be passed to the game.html template
		args = {'category': current_category_text}
		return redirect('play/', args)
	# Otherwise display the index view so the user can choose a category 
	else:
		# Clear saved words list if any exist
		clearAllSavedWords()
		# All categories saved in the database
		category_list = Category.objects.all()
		return render(request, 'game/index.html', {'category_list': category_list})

# INDEX VIEW FUNCTIONS

# The saveCurrentCategory function saves the category chosen by the user to be played
# @params request The http request i.e. GET POST


def saveCurrentCategory(request):
	current_category = CurrentCategory.objects.get()
	current_category.current_category_text = request.POST['category']
	current_category.save()
	return current_category.current_category_text

# THE GAME VIEW


def game(request):

	if request.method == 'POST':
		# The current category saved in the database
		current_category = CurrentCategory.objects.get()
		# The saved words saved in the database
		saved_words = SavedWord.objects.all()
		# The current score of the player during gameplay
		# This score is saved to the database
		current_score = calculateScore(100)
		# The current word displayed to the user during gameplay
		current_word = saveCurrentWord(request)
		# Add the current word to the list of saved words
		addSavedWord(request)
		# Arguments to be passed to the game.html template
		args = {
			'category': current_category.current_category_text,
			'current_word': current_word.current_word_text,
			'saved_words': saved_words,
			'letter_guess': current_word.current_word_text[-1].upper(),
			'current_score': current_score
		}
		return render(request, 'game/game.html', args)
	else:
		current_category = CurrentCategory.objects.get(id=1)
		# Clear the users score when the game starts
		clearSavedScore()
		# Clear the saved words when the game starts
		clearAllSavedWords()
		return render(request, 'game/game.html', {'category': current_category.current_category_text})

# GAME VIEW FUNCTIONS


# Clear user's score when game loads


def clearSavedScore():
	CurrentScore.objects.all().delete()

# The clearAllSavedWords function deletes all saved words from the database


def clearAllSavedWords():
	SavedWord.objects.all().delete()

# The addSavedWord function adds a new word to the list of saved words
# @params request The http request i.e. GET POST


def addSavedWord(request):
	# Create a saved word object
	saved_word = SavedWord(saved_word_text=request.POST['current_word'])
	# Save the word into the database
	saved_word.save()
	return saved_word

# The saveCurrentWord function takes the users input from the post request 
# and saves it into the database
# @params request The http request i.e. GET POST


def saveCurrentWord(request):
	# If the current word exists
	if CurrentWord.objects.get():
		# Set current word to the current word in the database
		current_word = CurrentWord.objects.get()
		# Change the current word text to the POST data
		current_word.current_word_text = request.POST['current_word']
		# Save the new current word into the database
		current_word.save()
	# If the current word does not exist
	else:
		# Create a new CurrentWord object
		current_word = CurrentWord(current_word_text=request.POST['current_word'])
		# Save the new word into the database
		current_word.save()
	return current_word

# The calculateScore function calculates the users score during gameplay
# @params score  The amount at which the score will increase


def calculateScore(score):
	try:
		current_score = CurrentScore.objects.get()
		# If score is zero reset the score to zero
		if score == 0:
			current_score.current_score_text = 0
			saveScore(current_score)
			return current_score.current_score_text
		# Add the score paramenter to the current score
		else:
			current_score.current_score_text = current_score.current_score_text + score
			saveScore(current_score)
			return current_score.current_score_text
	except CurrentScore.DoesNotExist:
		print("we got here")
		current_score = CurrentScore(current_score_text=score)
		saveScore(current_score)
		return current_score.current_score_text


# Save the score to the database


def saveScore(score):
	score.save()

# THE INSTRUCTIONS VIEW


def instructions(request):
	return render(request, 'game/instructions.html')

# THE SCORES VIEW


def scores(request):
	clearAllSavedWords()
	return render(request, 'game/scores.html')

# THE PROFILE VIEW


def profile(request):
	return render(request, 'game/profile.html')



		
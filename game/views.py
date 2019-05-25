# views.py
# Created by Joshua Clark on 5/20/19

from django.shortcuts import render, redirect
from game.models import Category, CurrentCategory, CurrentWord, SavedWord, CurrentScore, HighScore, PreviousWord

# THE INDEX VIEW


def index(request):
	# If a category was chosen, save the category and proceed to the game view
	if request.method == 'POST':
		# Save the current category to be used during gameplay
		current_category_text = saveCurrentCategory(request)
		# Arguments to be passed to the game.html template
		args = {
			'category': current_category_text
		}
		return redirect('play/', args)
	# Otherwise display the index view so the user can choose a category 
	else:
		# Clear saved words list if any exist
		clearAllSavedWords()
		# Set the score to 0 by default
		calculateScore(0)
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
		# Get the saved words saved in the database in reverse order
		# to display to the UI
		saved_words = SavedWord.objects.all().order_by('-id')
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
		clear_saved_score()
		# Set the score back to zero just in case the user doesn't
		# play the game at all.  If no score is entered it will break
		# the application, so we set 0 here.
		calculateScore(0)
		# Clear the saved words when the game starts
		clearAllSavedWords()
		return render(request, 'game/game.html', {'category': current_category.current_category_text})

# GAME VIEW FUNCTIONS


# Get previous word


def get_previous_word():
	SavedWord.objects.get()

# Clear user's score when game loads


def clear_saved_score():
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
		current_score = CurrentScore(current_score_text=score)
		saveScore(current_score)
		return current_score.current_score_text


# Save the score to the database


def saveScore(score):
	score.save()


# THE SCORES VIEW


def scores(request):
	# Clear all saved words from the database
	clearAllSavedWords()
	# Grab the current score from the recently played game
	current_score = CurrentScore.objects.get()
	high_scores = HighScore.objects.all().order_by('-score')[:10]
	if request.method == 'POST':
		# Get the user's name from the form
		username = request.POST['username']
		# Create a high score entry
		user_score = HighScore(score=current_score, username=username)
		# Save into high scores database.  If it is high enough, it will show in the top 10
		user_score.save()
	args = {
		'high_scores': high_scores,
		'current_score': current_score.current_score_text,
	}
	print('or we got here')
	return render(request, 'game/scores.html', args)

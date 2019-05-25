from django.db import models
import datetime

# Create your models here.


class Category(models.Model):
	class Meta:
		verbose_name_plural = "categories"
	category_text = models.CharField(max_length=200)

	def __str__(self):
		return self.category_text


class CurrentCategory(models.Model):
	class Meta:
		verbose_name_plural = "current categories" 
	current_category_text = models.CharField(max_length=200)

	def __str__(self):
		return self.current_category_text


class CurrentWord(models.Model):
	current_word_text = models.CharField(max_length=200)

	def __str__(self):
		return self.current_word_text


class PreviousWord(models.Model):
	previous_word_text = models.CharField(max_length=200)

	def __str__(self):
		return self.previous_word_text


class SavedWord(models.Model):
	saved_word_text = models.CharField(max_length=200)
	date = datetime.datetime.now()

	def __str__(self):
		return self.saved_word_text


class CurrentScore(models.Model):
	current_score_text = models.IntegerField()

	def __int__(self):
		return self.current_score_text


class HighScore(models.Model):
	score = models.IntegerField()
	username = models.CharField(max_length=200)

	def __int__(self):
		return self.score

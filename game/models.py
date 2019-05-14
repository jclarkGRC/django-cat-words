from django.db import models

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
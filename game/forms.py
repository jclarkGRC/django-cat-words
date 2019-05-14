from django import forms
from game.models import CurrentCategory, Category

class CurrentCategoryForm(forms.ModelForm):
	CHOICES = (
			('1','ME'),
			('2','YOU'),
			('3','WE'),
		)
	currentCategory = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

	class Meta:
		model = CurrentCategory
		fields = (
			'current_category_text',
		)

	def save(self, commit=True):
		if commit:
			currentCategory.save()

		return currentCategory



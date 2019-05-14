from django import forms
from game.models import CurrentWord

class CurrentWordForm(forms.ModelForm):
	
	class Meta:
		model = CurrentWord
		fields = (
			'current_word',
		)

	def save(self, commit=True):
		current_word = super(CurrentWordForm, self).save(commit=True)


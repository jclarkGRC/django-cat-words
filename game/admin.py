from django.contrib import admin

# Register your models here.

from .models import Category, CurrentCategory, CurrentWord, SavedWord, CurrentScore

admin.site.register(Category)
admin.site.register(CurrentCategory)
admin.site.register(CurrentWord)
admin.site.register(SavedWord)
admin.site.register(CurrentScore)
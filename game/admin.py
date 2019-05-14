from django.contrib import admin

# Register your models here.

from .models import Category, CurrentCategory

admin.site.register(Category)
admin.site.register(CurrentCategory)
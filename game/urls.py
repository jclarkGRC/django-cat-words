from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
	path('', views.index, name='index'),
	path('play/', views.game, name="game"),
	path('scores/', views.scores, name="scores"),
	path('instructions/', views.instructions, name="instructions"),
	path('profile/', views.profile, name="profile"),
]
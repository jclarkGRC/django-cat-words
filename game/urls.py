from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('play/', views.game, name="game"),
	path('scores/', views.scores, name="scores"),
	path('profile/', views.profile, name="profile"),
]
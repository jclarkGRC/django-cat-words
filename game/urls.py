from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
	path('', views.home, name="home"),
	path('play/', views.game, name="game")
]
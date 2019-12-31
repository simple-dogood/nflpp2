from django.urls import path

from . import views

urlpatterns =[
path('',views.game_results, name = 'game_results'),
path('games/',views.games_view,name = 'games_view'),
]

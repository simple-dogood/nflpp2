from django.urls import path

from . import views

urlpatterns =[
path('',views.view_games, name = 'view_games'),

]

from django.db import models
import os
from django.forms import ModelForm

class games_new(models.Model):
    Game_ID = models.CharField(max_length = 10,unique=True)
    Team1 = models.CharField(max_length=30)
    Team2 = models.CharField(max_length=30)
    Spread = models.FloatField()
    Total = models.FloatField()

    def __str__(self):
        return self.Game_ID



class Choice(models.Model):
    player = models.CharField(max_length = 30)
    game = models.ForeignKey(games_new, on_delete=models.CASCADE)
    team_selected = models.CharField(max_length=30)
    total_selected = models.CharField(max_length=10)

    def __str__(self):
        return self.game

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['player','game','team_selected','total_selected']

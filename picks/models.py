from django.db import models
import os
from django.forms import ModelForm


game_1 = (('Buffalo','Buffalo'),('Houston','Houston'))


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
    game = models.CharField(max_length=30,default='')
    team_selected = models.CharField(max_length=30)
    total_selected = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    tst = models.CharField(max_length=30,default='X')

    def __str__(self):
        return str(self.player)

from django.db import models


class games(models.Model):
    week = models.CharField(max_length = 10)
    t1 = models.CharField(max_length=30)
    t2 = models.CharField(max_length=30)
    spread = models.FloatField()
    ou = models.FloatField()

class results(models.Model):
    player = models.CharField(max_length=30)
    game = models.CharField(max_length=100)
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    playerpick = models.CharField(max_length=30)
    spread = models.FloatField()


class ply_results(models.Model):
    player = models.CharField(max_length=30)
    game_id = models.CharField(max_length=30)
    team_selection = models.CharField(max_length=30)
    ou = models.FloatField()
    points = models.FloatField()

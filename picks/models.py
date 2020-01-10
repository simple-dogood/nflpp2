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
    g_id = str(player)+"_"+str(game)
    tst4 = models.CharField(max_length=30,default='')


    def __str__(self):
        return str(self.player)


class Stand(models.Model):
    player = models.CharField(max_length=30)
    score = models.IntegerField()

class PickManager(models.Manager):
    def last_pick(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT DISTINCT g_id, player, team_selected, total_selected, created
            FROM picks_Choice2 Order By created DESC""")
            result_list = []
            for row in cursor.fetchall():
                p = self.model(player=row[0],team_selected=row[1],total_selected=row[2],created=row[4])
                result_list.append(p)
        return result_list

class Choice2(models.Model):
    player = models.CharField(max_length = 30)
    game = models.CharField(max_length=30)
    team_selected = models.CharField(max_length=30)
    total_selected = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    g_id = models.CharField(max_length=50)
    objects = PickManager()

    def save(self,*args,**kwargs):
        self.g_id = str(self.player)+"_"+str(self.game)
        super(Choice2,self).save(*args, **kwargs)





    def __str__(self):
        return str(self.player)

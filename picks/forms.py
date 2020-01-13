

from django import forms
from django.forms import ModelForm
from .models import Choice2

players = (('Select Name','Select Name'),('Pex','Pex'),('Mac','Mac'),('Mullen','Mullen'),('Bdoc','Bdoc'),('Campbell','Campbell'),('Harbs','Harbs'),('Meat','Meat'),('Minas','Minas'),('Tony','Tony'))

match_ups = (('Minnesota','Minnesota'),('San Fran','San Fran'),('Tennessee','Tennessee'),('Baltimore','Baltimore'),('Houston','Houston'),('Kansas City','Kansas City'),('Seattle','Seattle'),('Green Bay','Green Bay'),)
match_ups = (('Clemson','Clemson'),('LSU','LSU'))

pwk = (('CFB','CFB'),('N/A','N/A'))

game_1_teams = (('Buffalo','Buffalo'),('Houston','Houston'))
game_2_teams = (('Tennessee','Tennessee'),('New England','New England'))
game_3_teams = (('Minnesota','Minnesota'),('New Orleans','New Orleans'))
game_4_teams = (('Seattle','Seattle'),('Philadelphia','Philadelphia'))

under_over = (('N/A','N/A'),('Under','Under'),('Over','Over'))

#
# class ChoiceForm(ModelForm):
#     class Meta:
#         model = Choice
#         fields = ['player','team_selected','total_selected']

class ChoiceForm1(ModelForm):
    game = forms.ChoiceField(choices=pwk,required=True)
    player = forms.ChoiceField(choices=players,required=True)
    team_selected = forms.ChoiceField(choices=match_ups,required=True)
    total_selected = forms.ChoiceField(choices=under_over,required=True)
    class Meta:
        model = Choice2
        fields = ['game','player','team_selected','total_selected']

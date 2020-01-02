

from django import forms
from django.forms import ModelForm
from .models import Choice

players = (('Select Name','Select Name'),('Mac','Mac'),('Mullen','Mullen'),('Bdoc','Bdoc'),('Campbell','Campbell'),('Harbs','Harbs'),('Meat','Meat'),('Minas','Minas'),('Tony','Tony'))

game_1_title = (('Buffalo vs. Houston','Buffalo vs. Houston'),)
game_2_title = (('Tennessee vs. New England','Tennessee vs. New England'),)
game_3_title = (('Minnesota vs. New Orleans','Minnesota vs. New Orleans'),)
game_4_title = (('Seattle vs. Philadelphia','Seattle vs. Philadelphia'),)

game_1_teams = (('Buffalo','Buffalo'),('Houston','Houston'))
game_2_teams = (('Tennessee','Tennessee'),('New England','New England'))
game_3_teams = (('Minnesota','Minnesota'),('New Orleans','New Orleans'))
game_4_teams = (('Seattle','Seattle'),('Philadelphia','Philadelphia'))

under_over = (('Under','Under'),('Over','Over'))


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['game','player','team_selected','total_selected']

class ChoiceForm1(ModelForm):
    game = forms.ChoiceField(choices=game_1_title,required=True)
    player = forms.ChoiceField(choices=players,required=True)
    team_selected = forms.ChoiceField(choices=game_1_teams,required=True)
    total_selected = forms.ChoiceField(choices=under_over,required=True)
    class Meta:
        model = Choice
        fields = ['game','player','team_selected','total_selected']

class ChoiceForm2(ModelForm):
    game = forms.ChoiceField(choices=game_2_title,required=True)
    player = forms.ChoiceField(choices=players,required=True)
    team_selected = forms.ChoiceField(choices=game_2_teams,required=True)
    total_selected = forms.ChoiceField(choices=under_over,required=True)
    class Meta:
        model = Choice
        fields = ['game','player','team_selected','total_selected']

class ChoiceForm3(ModelForm):
    game = forms.ChoiceField(choices=game_3_title,required=True)
    player = forms.ChoiceField(choices=players,required=True)
    team_selected = forms.ChoiceField(choices=game_3_teams,required=True)
    total_selected = forms.ChoiceField(choices=under_over,required=True)
    class Meta:
        model = Choice
        fields = ['game','player','team_selected','total_selected']

class ChoiceForm4(ModelForm):
    game = forms.ChoiceField(choices=game_4_title,required=True)
    player = forms.ChoiceField(choices=players,required=True)
    team_selected = forms.ChoiceField(choices=game_4_teams,required=True)
    total_selected = forms.ChoiceField(choices=under_over,required=True)
    class Meta:
        model = Choice
        fields = ['game','player','team_selected','total_selected']

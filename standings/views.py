from django.shortcuts import render, get_object_or_404
from .models import results, games


def game_results(request):
    rkd = results.objects
    return render(request,'standings/standings.html',{'rkd':rkd})

def games_view(request):
    gamez = games.objects
    return render(request,'standings/game.html',{'gamez':gamez})

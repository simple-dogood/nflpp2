from django.shortcuts import render
from .models import games_new,Choice2
from .forms import ChoiceForm, ChoiceForm1#, ChoiceForm2, ChoiceForm3, ChoiceForm4
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory

def view_games(request):
    gms = games_new.objects
    chc = Choice2.objects


    if request.method == 'POST':
        form1 = ChoiceForm1(request.POST)
        if form1.is_valid():
            u = form1.save()
            return HttpResponseRedirect('/picks/')
    else:
        form1 = ChoiceForm1()



    return render(request,'picks/schedule_n_picks.html',{'gms':gms,'form1':form1,'chc':chc})

from django.shortcuts import render
from .models import games_new,Choice2, Stand
from .forms import ChoiceForm1#, ChoiceForm2, ChoiceForm3, ChoiceForm4
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory

def view_games(request):
    stnd = Stand.objects
    gms = games_new.objects
    chc = Choice2.objects
    chc_slct = Choice2.last_pick.result_list


    if request.method == 'POST':
        form1 = ChoiceForm1(request.POST)
        if form1.is_valid():
            u = form1.save()
            return HttpResponseRedirect('/picks/')
    else:
        form1 = ChoiceForm1()



    return render(request,'picks/schedule_n_picks.html',{'stnd':stnd,'gms':gms,'form1':form1,'chc':chc,'chc_slct':chc_slct})

from django.shortcuts import render
from .models import games_new,Choice
from .forms import ChoiceForm, ChoiceForm1, ChoiceForm2, ChoiceForm3, ChoiceForm4
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory

def view_games(request):
    gms = games_new.objects
    chc = Choice.objects


    if request.method == 'POST':
        form1 = ChoiceForm1(request.POST)
        if form1.is_valid():
            u = form1.save()
            return HttpResponseRedirect('/picks/')
    else:
        form1 = ChoiceForm1()

    if request.method == 'POST':
        form2 = ChoiceForm2(request.POST)
        if form2.is_valid():
            u = form2.save()
            return HttpResponseRedirect('/picks/')
    else:
        form2 = ChoiceForm2()

    if request.method == 'POST':
        form3 = ChoiceForm3(request.POST)
        if form3.is_valid():
            u = form3.save()
            return HttpResponseRedirect('/picks/')
    else:
        form3 = ChoiceForm3()

    if request.method == 'POST':
        form4 = ChoiceForm4(request.POST)
        if form4.is_valid():
            u = form4.save()
            #return HttpResponseRedirect('/picks/')
    else:
        form4 = ChoiceForm4()



    return render(request,'picks/schedule_n_picks.html',{'gms':gms,'form1':form1,'form2':form2,'form3':form3,'form4':form4,'chc':chc})

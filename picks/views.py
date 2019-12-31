from django.shortcuts import render
from .models import games_new, ChoiceForm

def view_games(request):
    gms = games_new.objects

    form = ChoiceForm(request.POST or None)
    error = None
    if form.is_valid():
        model_instance = form.save(commit=True)
        #model_instance.timestamp = timezone.now()
        #model_instance.save()
        

    else:

        form = ChoiceForm()

    return render(request,'picks/schedule_n_picks.html',{'gms':gms,'form': form})

# def view_form(request):
#
#
#         return render(request, "picks/schedule_n_picks.html", )

#  fields = ['player','game','team_selected','total_selected']

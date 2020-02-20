from django.shortcuts import render
from .models import Timery
import datetime
from django.http import HttpResponseRedirect
from datetime import timedelta

# Create your views here.


def index(request):
    queryset = Timery.objects.all()
    context = {
        "object_list": queryset}
    return render(request, 'timers/list.html', context)

def add(request):
    now = 0
    if request.method == 'POST':
        nazwa = request.POST.get("nazwa")
        dni = request.POST.get("dni")
        godziny = request.POST.get("godziny")
        minuty = request.POST.get("minuty")
        now = datetime.datetime.now() + timedelta(days=int(dni),hours=int(godziny)+1,minutes=int(minuty))
        now = now.strftime("%m/%d/%Y, %H:%M:%S")
        add_to_db = Timery.objects.create(nazwa=nazwa, date1=now)
        return HttpResponseRedirect('/')


    else:
        return render(request, 'timers/add.html', {'dupa': now})


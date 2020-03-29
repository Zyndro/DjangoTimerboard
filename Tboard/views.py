from django.shortcuts import render
from .models import Timery
import datetime
from django.http import HttpResponseRedirect
from datetime import timedelta

# Create your views here.


def index(request):

    queryset = Timery.objects.order_by('date1')
    context = {
        "object_list": queryset}


    print(context)
    return render(request, 'timers/list.html', context)

def add(request):
    now = 0
    if request.method == 'POST':
        try:
            nazwa = request.POST.get("nazwa")
            dni = request.POST.get("dni")
            godziny = request.POST.get("godziny")
            minuty = request.POST.get("minuty")
            now = datetime.datetime.now() + timedelta(days=int(dni),hours=int(godziny)+2,minutes=int(minuty))
            now = now.strftime("%m/%d/%Y, %H:%M:%S")
            add_to_db = Timery.objects.create(nazwa=nazwa, date1=now)
            return HttpResponseRedirect('/')
        except:
            return render(request, 'timers/error.html')


    else:
        return render(request, 'timers/add.html', {'dupa': now})


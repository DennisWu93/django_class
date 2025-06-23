from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.

def index(request):
    nowdate = datetime.datetime.now()
    return render(request, "newyear/index.html",{"newyear":nowdate.month == 1 and nowdate.day == 1})


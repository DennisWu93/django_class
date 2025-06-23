from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def Dennis(request):
    return HttpResponse("Hello, Dennis.")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}.")
    return render(request, "hello/greet.html",{"name":name.capitalize()})
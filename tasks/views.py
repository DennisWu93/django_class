
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

#can create tasks when request, then mute below line and add lines 14-15
# tasks = ['foo', 'bar', 'baz']

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task', max_length=100)
    # priority = forms.IntegerField(label='Priority', min_value=1, max_value=10)
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{"tasks": request.session["tasks"]})

def add(request):
    #if the user submits data
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})
    #if the users just get the data
    return render(request, "tasks/add.html", {"form": NewTaskForm()})


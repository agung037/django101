from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(requests):
    if "tasks" not in requests.session:
        requests.session["tasks"] = []

    return render(requests, "tasks/index.html", {
        "tasks": requests.session["tasks"]
    })

def add(requests):
    if requests.method == "POST":
        form = NewTaskForm(requests.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            requests.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(requests, "tasks/add.html", {
                "form": form
            })

    return render(requests, "tasks/add.html", {
        "form": NewTaskForm()
    })
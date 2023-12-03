
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

from django.template import loader

def checklistform(request):
    for name in request.POST:
        print("{}: {}".format(name,
        request.POST.getlist(name)))
    return render(request, "studentform2.html", {"method":
request.method})

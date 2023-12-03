
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

def checklistform(request):
    return HttpResponse("Welcome to CIDM 6395 Project for Megan Moore!")



from django.template import loader

def checklistform(request):
    for name in request.POST:
        print("{}: {}".format(name,
        request.POST.getlist(name)))
    return render(request, "studentform2.html", {"method":
request.method})



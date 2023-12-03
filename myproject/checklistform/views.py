
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

#def checklistform(request):
#    return HttpResponse("Welcome to CIDM 6395 Project for Megan Moore!")

def checklistform(request):
  template = loader.get_template('welcome.html')
  return HttpResponse(template.render())

from django.shortcuts import render
def welcome_view (request):
    return render(request, 'welcome.html')

from django.template import loader

def checklistform(request):
    for name in request.POST:
        print("{}: {}".format(name,
        request.POST.getlist(name)))
    return render(request, "studentform2.html", {"method":
request.method})



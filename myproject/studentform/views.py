
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

from django.template import loader

def studentform(request):
    for name in request.POST:
        print("{}: {}".format(name,
        request.POST.getlist(name)))
    return render(request, "studentform1.html", {"method":
request.method})

#def studentform(request):
#    return render(request, "form-example.html")

#def studentform(request):
#    return render(request, "studentform1.html")

#def studentform(request):
#    if request.method == "POST":
#        form = studentform(request.POST)
#        if form.is_valid():
#            for name, value in form.cleaned_data.items():
#                print("{}: ({}) {}".format(name, type(value), value))
#    else:
#        form = studentform()
#
#    return render(
#        request, "studentform1.html", {"method": request.method, "form": form}
#    )

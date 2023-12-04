
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

def welcome_view(request):
       message = f"<html><h1>Welcome to CIDM 6325 landing page!</h1></html>"
       return HttpResponse(message)

from .forms import PublisherForm, SearchForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Professor, WTStaff
from django.contrib import messages

def publisher_edit(request, pk=None):
    if pk is not None:
        WTStaff = get_object_or_404(WTStaff,
        pk=pk)
    else:
        WTStaff = None
    if request.method == "POST":
        form = PublisherForm(request.POST,
        instance=WTStaff)
        if form.is_valid():
            updated_publisher = form.save()
            if WTStaff is None:
                messages.success(request, "WTStaff
                "{}" was created."
                .format(updated_publisher))
            else:
                messages.success(request, "WTStaff
                "{}" was updated."
                .format(updated_publisher))
            return redirect("publisher_edit",
            updated_publisher.pk)
    else:
        form = PublisherForm(instance=WTStaff)
        return render(request, "form-example.html",
    {"method": request.method, "form": form})
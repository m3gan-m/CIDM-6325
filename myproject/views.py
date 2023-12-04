from django.shortcuts import render
from django.http import HttpResponse

def checklistform(request):
    return HttpResponse("Welcome to CIDM 6395 Project for Megan Moore!")

initial = {"email": "user@example.com"}

from .forms import PublisherForm, SearchForm
# two types of view: class based view & function based view
# we start with function based view

# two types: class based view & function based view

# two types: class based view & function based view

from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse("<h1>My First Django APP!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current Date & Time:</b> " + str(dt)
    return HttpResponse(s)






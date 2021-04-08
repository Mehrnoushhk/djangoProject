from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


def welcome(request):
    meetings = Meeting.objects.all()
    return render(request, 'website/welcome.html', {'meetings': meetings})


def date(request):
    return HttpResponse("Welcome to the Meeting Planner" + str(datetime.now()))


def about(request):
    return HttpResponse("I AM AWESOME!")

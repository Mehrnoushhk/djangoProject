from django.shortcuts import render, redirect
from .models import Meeting, Room
from django.forms import modelform_factory


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})


def rooms_details(request):
    return render(request, 'meetings/rooms.html', {'rooms': Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})
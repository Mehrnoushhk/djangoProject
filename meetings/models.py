from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField()

    def __str__(self):
        return f'{self.name}: ' \
               f'Room {self.room_number} at floor {self.floor_number}'


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE,
                             default='1')

    def __str__(self):
        return f'{self.title} at {self.start_time} ' \
               f'on {self.date} in {self.room}'

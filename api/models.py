from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import validate_email
import random

import datetime


def validateUsername(username):
    if ' ' in username:
        raise ValidationError("Username contains whitespace. Submitted: " + username)

class User(models.Model):
    userName = models.CharField(max_length=50, blank=False, unique=True)
    email = models.CharField(max_length=100, blank=False, primary_key=True, validators=[validate_email])
    passwordHash = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f"(User: {self.userName}, {self.email})"

class Schedule(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    dateCreated = models.DateField(default=datetime.date.today)
    name = models.CharField(default=datetime.date.today, max_length=75)

    def __str__(self):
        return f"(Schedule: {self.author}, {self.dateCreated})"

class Goal(models.Model):
    scheduleId = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    goal = models.CharField(max_length=100)
    priority = models.IntegerField()

class Block(models.Model):
    scheduleId = models.ForeignKey('Schedule', on_delete=models.CASCADE)

    hourChoices = (
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
        (13, "13"),
        (14, "14"),
        (15, "15"),
        (16, "16"),
        (17, "17"),
        (18, "18"),
        (19, "19"),
        (20, "20"),
        (21, "21"),
        (22, "22"),
        (23, "23"),
        (24, "24"),
    )
    hour = models.IntegerField(choices=hourChoices)

    minuteChoices = (
        (0, "00"),
        (30, "30"),
    )
    minute = models.IntegerField(choices=minuteChoices)
    content = models.CharField(max_length=100)
    length = models.IntegerField(default=1)

    colorList = ["#0af9fb", "#e6093f", "#f5bd33", "#ef988e", "#6c922c"]

    def randomColor(self):
        return random.choice(self.colorList)

    color = models.CharField(default=randomColor, max_length=7)




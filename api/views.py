from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import User, Schedule, Block, Goal
from .serializers import UserSerializer, ScheduleSerializer, BlockSerializer, GoalSerializer
# Create your views here.

def index(request):
    return HttpResponse("Testing.")

def getSchedule(request, userId, scheduleId):
    return HttpResponse(f"TEST getting user:{userId} schedule:{scheduleId}")

def getUser(request, userId):
    return HttpResponse(f"TEST getting info on user: {userId}")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('author')
    serializer_class = ScheduleSerializer

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all().order_by('hour')
    serializer_class = BlockSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all().order_by('priority')
    serializer_class = GoalSerializer


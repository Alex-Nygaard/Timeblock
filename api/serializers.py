from rest_framework import serializers
from .models import User, Schedule, Block, Goal

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userName', 'email')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('userName', 'email', 'name')


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = ('scheduleId', 'hour', 'minute', 'content', 'length', 'color')

class GoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goal
        fields = ('scheduleId', 'goal', 'priority')


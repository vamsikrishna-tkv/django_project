from rest_framework import serializers
from .models import ActivityPeriod,Users

# first we need to define the activity period class so that we can use in UsersSerializer class
class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields =[
            'start_time',
            'end_time',
        ]

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    activity_periods=ActivityPeriodSerializer (many=True,read_only=True) # This reference 'activity_periods' is delcared in the models.py file
    # Here activity_periods is the list of tuples for the one to many relation between user and activity
    class Meta:
        model = Users
        fields =[
            'id',
            'real_name',
            'tz',
            'activity_periods',
        ]
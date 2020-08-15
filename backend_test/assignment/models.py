from django.db import models

# Creating 2 models as per the requirement
class Users(models.Model):
    id = models.CharField(primary_key=True,max_length=20)  # This is the id field and its a primary key
    real_name = models.CharField(max_length=100) # This is a character attribute
    tz = models.CharField(max_length=100) # This is a character attribute

    def __str__(self):
        return self.id

class ActivityPeriod(models.Model):
    start_time = models.CharField(max_length=100) # This is a attribute for the activity
    end_time = models.CharField(max_length=100) # This is a attribute for activity
    user = models.ForeignKey(Users,related_name='activity_periods',on_delete=models.CASCADE) # This is a foreign key relation to the users model above

    def __str__(self):
        return self.start_time
# Create your models here.

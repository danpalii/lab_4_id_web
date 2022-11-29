from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=100)
    event_description = models.CharField(max_length=100)
    # event_location = models.CharField(max_length=100)
    # event_date = models.DateField()

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)





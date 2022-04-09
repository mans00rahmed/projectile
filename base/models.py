from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return(self.name)

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True) 

    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    #participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return(self.name)


class Message(models.Model):
    #this is to make a relation of 1-Many in code,b y adding foreign key...
    user = models.ForeignKey(User,on_delete=models.CASCADE) # this cas casde will delete all message once room is deleted.
    room = models.ForeignKey(Room,on_delete=models.CASCADE) # this cas casde will delete all message once room is deleted.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return(self.body[0:50])
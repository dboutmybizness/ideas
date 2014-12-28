from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 100)

class Note(models.Model):
    idea = models.ForeignKey(Idea)
    txt = models.TextField()
    created_time = models.DateTimeField(auto_now_add = True)
    modified_time = models.DateTimeField(auto_now = True)
from django.db import models
from django.contrib.auth.models import User


class Idea_Type(models.Model):
    idea_type = models.CharField(max_length = 50)
    industries = (
        ('TECHNOLOGY', 'Technology'),
        ('MASS_MEDIA', 'Mass Media'),
        ('GEN', 'General'),
    )

    idea_industry = models.CharField(max_length=25, choices=industries)
    def __unicode__(self):
        return self.idea_type

class Idea(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    idea_type = models.ForeignKey(Idea_Type, null = True, blank=True)
    short_description = models.CharField(max_length = 254, blank=True)
    full_description = models.TextField(blank=True)
    initial_summary = models.TextField(blank=True, null=True)
    #created_date = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add = True, null = True)

    def link(self):
        return '/ideas/%d/' % (self.id)

    

    def notes(self):
        return Note.objects.filter(idea = self).order_by('-created_time')

    def __unicode__(self):
        return self.name

class Note(models.Model):
    idea = models.ForeignKey(Idea)
    headline = models.CharField(max_length = 140, blank = True)
    txt = models.TextField()
    created_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add = True)
    modified_time = models.DateTimeField(auto_now = True)

    def link(self):
        return '/ideas/%d/note/%d/' % (self.idea.id, self.id)

    def headline_echo(self):
        return (self.headline if self.headline else 'Untitled')

    def __unicode__(self):
        return '%s - %s' % (self.idea,self.txt[:75])

class Recently_Viewed(models.Model):
    idea = models.ForeignKey(Idea)
    user = models.ForeignKey(User)
    viewed_time = models.DateTimeField()
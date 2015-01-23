from django.conf.urls import patterns, include, url

urlpatterns = patterns('ideas.views',
	url(r'^$', 'dash'),
	url(r'^(?P<id>\d+)/$', 'idea_landing'),
	url(r'^(?P<idea_id>\d+)/note/(?P<note_id>\d+)/$', 'note_landing'),
	url(r'^list/$', 'ideas_main'),

)
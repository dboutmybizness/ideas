from django.conf.urls import patterns, include, url

urlpatterns = patterns('ideas.views',
	url(r'^$', 'dash'),
	url(r'^(?P<id>\d+)/$', 'idea_landing'),
	url(r'^list/$', 'ideas_main'),
)
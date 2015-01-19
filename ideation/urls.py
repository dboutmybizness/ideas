from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ideation.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('ideas.views',
	url(r'^$', 'dash'),
	url(r'^ideas/(?P<id>\d+)/$', 'idea_landing'),
	url(r'^ideas/$', 'ideas_main'),
)
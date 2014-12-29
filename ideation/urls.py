from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ideation.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('ideas.views',
	url(r'^$', 'main'),
	url(r'^idea/(?P<id>\d+)/$', 'idea_landing'),
	url(r'^idea/$', 'idea_create'),
)
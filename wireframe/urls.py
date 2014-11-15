from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wireframe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^g43exercise/', include('g43exercise.urls', namespace="g43")),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, url
from g43exercise import views
from django.conf.urls.static import static
from django.conf import settings

# Create your urls patterns here.
urlpatterns = patterns('',
	# The index page /g43exercise
	url(r'^$', views.index, name='index'),
	# The article detail page 
	# ex. /g43exercise/1
	url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),
	# Any media elements found in the media directory
	# ex. /g43exercise/media/heroes/filename.jpg
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
	}, name='media'),
	# Any static elements found in the static directory
	# ex. /g43exercise/static/css/style.css
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.STATIC_ROOT,
	}),
)
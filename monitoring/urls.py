from django.conf.urls import patterns, url
from monitoring import views

urlpatterns = patterns('',
	url(r'^$', views.locations_view),
	url(r'^sensors$', views.locations_view),
	url(r'^readings/(?P<sensor_id>\d+?)/$', views.readings_view),
	url(r'^register/$', views.register_user),
	url(r'^register/success/$', views.register_success),
)
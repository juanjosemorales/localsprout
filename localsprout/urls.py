from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('monitoring.urls')),
    url(r'^monitoring/', include('monitoring.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

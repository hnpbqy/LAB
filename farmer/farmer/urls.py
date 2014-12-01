from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'farmer.views.home', name='home'),
    # url(r'^farmer/', include('farmer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'farmer.views.home', name='home'),
    url(r'^detail/(?P<id>\d+)/$', 'farmer.views.detail', name='detail'),
    url(r'^retry/(?P<id>\d+)/$', 'farmer.views.retry', name='retry'),
    url(r'^rerun/(?P<id>\d+)/$', 'farmer.views.rerun', name='rerun'),
)

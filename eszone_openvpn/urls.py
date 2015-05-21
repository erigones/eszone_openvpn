from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:1
    # url(r'^$', 'eszone_openvpn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('api_openvpn.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls', namespace='admin')),
)

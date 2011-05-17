# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    (r'^inscricao/', include('contato.urls', namespace='contato')),
)

# Static URL
urlpatterns += staticfiles_urlpatterns()


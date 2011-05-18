from django.conf.urls.defaults import patterns, include, url
from tools.route import route

urlpatterns = patterns('contato.views',
    route(r'^$',GET='add_contato',POST='save_contato',name='contato'),
    url(r'(\d+)/sucesso/$', 'sucesso', name='sucesso'),
)

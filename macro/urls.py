from django.conf.urls import patterns, url

from macro import views

urlpatterns = patterns('macro.views',
    url(r'^$', 'index'),
    url(r'^settings/$', 'settings'),
    url(r'^settings/power/$', 'power'),
)
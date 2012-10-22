from django.conf.urls import patterns, url

from macro import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')                       
)
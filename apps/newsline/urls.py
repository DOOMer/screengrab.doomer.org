# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

from newsline import views

urlpatterns = patterns('',
    url(r'^$', views.News.as_view()),
)
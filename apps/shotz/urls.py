# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('apps.shotz.views',
	url(r'^$', ScreenshotListView.as_view(), name='shots-view'),
	url(r'^old/$', ScreenshotListView.as_view(), kwargs={'old': True,}, name='shots-view-old'),
)

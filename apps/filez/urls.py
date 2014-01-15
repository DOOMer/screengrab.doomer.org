# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$', CurrentFilesView.as_view(), name='files-current'),
    url(r'^old/$', OldFilesView.as_view(), name='files-old'),
    #url(r'^(?P<file_name>[^/]+)/$', FileRedirectView.as_view(), name='files-get'),
    url(r'^(?P<file_name>[^/]+)/$', get_file, name='files-get'),
)
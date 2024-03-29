# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^feedback/', include("feedback_form.urls", namespace="feedback_form")),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^blackdoor/', include(admin.site.urls)),
    
    # news
    url(r'^news/', include('newsline.urls')), 

    # shots
	url(r'^shots/', include('shotz.urls')),

    # downloads
    url(r'^download/', include('filez.urls')), 
    
    # ck editor
    url(r'^ckeditor/', include('ckeditor.urls')), 
    
    # It Works!!!!
	url(r'^(?P<alias>.*)$', 'apps.pages.views.display_page'),
)

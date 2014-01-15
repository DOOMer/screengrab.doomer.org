# -*- encoding: utf-8 -*-

# import models
from apps.pages.models import Page

# import shortcut
from django.shortcuts import render_to_response, get_object_or_404

# response redirect import
from django.http import HttpResponse, HttpResponseRedirect
#from django.http import HttpResponseRedirect

# request context
from django.template import loader, RequestContext

# import asfe filter
from django.utils.safestring import mark_safe

# import settings
from django.conf import settings

def display_page(request, alias):

	if not alias.startswith('/'):
		alias = "/" + alias

	# получаем объект
	pg = get_object_or_404(Page, url = alias)
		
	# mark the title and content as already safe (since they are raw HTML
	pg.title = mark_safe(pg.title)
	pg.content = mark_safe(pg.content)
	
	if  pg.meta_description == "":
		pg.meta_description = settings.META_DESCRIPTION
	
	if  pg.meta_keywords == "":
		pg.meta_keywords = settings.META_KEYWORDS

	template_name = "pages/page.html"
	if alias == "/":
		template_name = "pages/main.html"
    
	# template loader
	t = loader.get_template(template_name)

	# request context
	c = RequestContext(request, {
		'page': pg, 		
	})
	
	# generate response on rendrer to context
	response = HttpResponse(t.render(c))

	return response
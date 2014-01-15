# -*- encoding: utf-8 -*-

from django.views.generic import ListView, RedirectView
from django.http import Http404, HttpResponseRedirect, HttpResponse

from models import FileModel

from os import path

class CurrentFilesView(ListView):
	template_name = "filez/filez_index.html"
	context_object_name = "file_list"
	queryset = FileModel.current.all()

class OldFilesView(ListView):
	template_name = "filez/filez_old.html"
	context_object_name = "file_list"
	queryset = FileModel.old.all()
	
def get_file(request, file_name):
	try:
		current_file = FileModel.objects.get(slug = file_name)
		current_file.loads_count = current_file.loads_count + 1
		current_file.save()
				
		url_to_redirect = path.split(current_file.file.url)
		response = HttpResponse()
		response["Content-Disposition"] = "attachment; filename=" + url_to_redirect[1]
		response["Content-Type"] = "application/octet-stream; charset=binary'"
		response['X-Accel-Redirect'] = current_file.file.url
		
		return response
	
	except FileModel.DoesNotExist:
		raise Http404
'''	
class FileRedirectView(RedirectView):
	permanent = False
	
	def get_redirect_url(self, **kwargs):
		if "file_name" not in self.kwargs :
			#print "not type"
			raise Http404
		else:
			#print "yes type"
			file_name = self.kwargs['file_name']
			
			try:
				current_file = FileModel.objects.get(slug = file_name)
				current_file.loads_count = current_file.loads_count + 1
				current_file.save()
				
				self.url = current_file.file.url
				
				return self.url
			except FileModel.DoesNotExist:
				raise Http404
			
	def get(self, request, *args, **kwargs):
		self.request.META['CONTENT_TYPE'] = "application/x-download"
		#print self.request.META
		
		response = super(FileRedirectView, self).get(self, request, *args, **kwargs)
		#response['Content-Disposition'] = 'attachment; filename=foo.xls'
		print response.headers	
		#['Content-Disposition']
		return response
'''	
		#return super(FileRedirectView, self).get(self, request, *args, **kwargs)
		#HttpResponseRedirect(self.url)
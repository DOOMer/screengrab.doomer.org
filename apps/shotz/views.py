# -*- encoding: utf-8 -*-

from django.views.generic.list import ListView
from models import ScreenshotModel

class ScreenshotListView(ListView):
	context_object_name = "screenshot_list"
	model = ScreenshotModel

	def dispatch(self, request, *args, **kwargs):
		if "old" in kwargs:
			self.old = True
		else:
			self.old = False

		return super(ScreenshotListView, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		qs = ScreenshotModel.objects.filter(old_version = self.old)
		return qs

	def get_template_names(self):
		if self.old:
			return "shotz/shots_list_old.html"
		else:
			return "shotz/shots_list.html"
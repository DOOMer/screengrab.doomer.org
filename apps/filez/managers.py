# -*- encoding: utf-8 -*-

from django.db import models

class CurrentReleaseManager(models.Manager):
	''' отдаем  queryset с картами, не помеченными как древние '''
	def get_query_set(self):
		return super(CurrentReleaseManager, self).get_query_set().exclude(version__exact = self.model.VERSION_OLD)
	#.order_by("-pub_date")

class OldReleaseManager(models.Manager):
#	''' отдаем  queryset с картами, не помеченными как древние '''
	def get_query_set(self):
		return super(OldReleaseManager, self).get_query_set().filter(version__exact = self.model.VERSION_OLD)


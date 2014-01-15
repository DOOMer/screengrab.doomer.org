# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models

from ckeditor.fields import RichTextField

class Page(models.Model):
	'''
	Класс для отображения простой страницы
	'''
	url = models.CharField(max_length=96, db_index=True)
	title = models.CharField(max_length=192)
	content = RichTextField(config_name='awesome_ckeditor')
	meta_description = models.TextField(blank=True, max_length=1024)
	meta_keywords = models.CharField(blank=True, max_length=128)
	#meta_keywords = RichTextField()

	class Meta:
		''' Meta information '''
		ordering = ('url',)
		verbose_name = _("flat page")
		verbose_name_plural = _("flat pages")
#		db_table = 'pages'
		
	
	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)
		
	def get_absolute_url(self):
		return self.url

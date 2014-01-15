# -*- encoding: utf-8 -*-

from django.db import models
from django.core.files.base import ContentFile
import apps.utils as utils

class ScreenshotModel(models.Model):
	file = models.ImageField(upload_to = utils.make_upload_path, verbose_name = u'Скриншот')
	thumb = models.ImageField(upload_to = utils.make_upload_path, blank = True, null = True)
	description = models.CharField(max_length = 255, blank = True, verbose_name = u'Описание ссылки')
	old_version = models.BooleanField(default = False, verbose_name = u'Старая версия')
	
	class Meta:
		verbose_name = u'Скриншот'
		verbose_name_plural = u'Скриншоты'

	def __unicode__(self):
		return self.description
	
	'''
		Get directory name for uploading
	'''
	def get_upload_path(self):
		return "screenshots"

	def save(self, force_insert=False, force_update=False, using=None):
		print "saving"
		# gen thumbs
		thumbs = utils.generate_thumbnail(self.file, self.get_upload_path())
		print self.file.storage
		# save generated thumbs
		self.thumb.save(thumbs['name'], ContentFile(thumbs['data'].getvalue()), False)

		super(ScreenshotModel, self).save(force_insert, force_insert,using)
		
	def delete(self, using=None):
		print "deleting "
		utils.kill_file(self.file.path)
		utils.kill_file(self.thumb.path)
		super(ScreenshotModel, self).delete()
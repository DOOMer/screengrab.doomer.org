# -*- encoding: utf-8 -*-

import datetime
from django.db import models
import managers
import apps.utils as utils

class FileModel(models.Model):
	VERSION_STABLE = 0
	VERSION_TESTING = 1
	VERSION_OLD = 2

	VERSION_CHOICES = (
		(VERSION_STABLE, 'Stable'),
		(VERSION_TESTING, 'Testing'),
		(VERSION_OLD, 'Old'),
	)

	title = models.CharField(max_length = 128, verbose_name = u'Тайтл')
	slug = models.SlugField(max_length = 256, help_text = u'Used in the URL of the entry.')
	file = models.FileField(upload_to = utils.make_upload_path, verbose_name = u'Файл')
	pub_date = models.DateTimeField(verbose_name = u'Дата публикации', default = datetime.datetime.today())
	version = models.IntegerField(verbose_name = u'Версия', choices = VERSION_CHOICES)
	loads_count = models.PositiveIntegerField(default=0, verbose_name = u'Количество скачиваний')

	objects = models.Manager()
	current = managers.CurrentReleaseManager()
	old = managers.OldReleaseManager()

	class Meta:
		ordering = ['-pub_date']
		verbose_name = 'File'
		verbose_name_plural = 'Files'

	def __unicode__(self):
		return self.title

	'''
		Generate slug from filename at saving
		Remove existing file for avoid duplication (on update obj)
	'''
	def save(self, *args, **kwargs):
		if self.id:
			file_to_kill = self.get_upload_path() + "/" + self.file.name
			utils.kill_file(file_to_kill)
				
		self.slug = utils.slugify(self.file.name)
		super(FileModel, self).save(*args, **kwargs)
		
	'''
		Kill existing file, when object is deleted
	'''
	def delete(self, using=None):
		utils.kill_file(self.file.path)		
		super(FileModel, self).delete()
		
	'''
		Get directory name for uploading
	'''
	def get_upload_path(self):
		return "downloads"
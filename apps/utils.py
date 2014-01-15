# -*- encoding: utf-8 -*-
from django.core.files.storage import default_storage
from PIL import Image
from os import path
from StringIO import StringIO
from django.conf import settings
from apps.shotz import settings as shotz_settings

'''
функция генерации пути для сохранения файла
instance — это экземпляр объекта модели, которой и принадлежит поле с типом FileField.
filename — юникодное имя файла.
'''
def make_upload_path(instance, filename):
	#  генерируем аплоад_ту на основе слуга категории файла
	return u"%s/%s" % (instance.get_upload_path(), filename)

'''
	Kill existing file
'''
def kill_file(file_path):
	#print file_path

	if default_storage.exists(file_path):
		default_storage.delete(file_path)

'''
	Create slug for uploaded files
'''
def slugify(name_to_slug):	
	slug = path.splitext(name_to_slug)[0]
	slug = path.split(slug)[-1]
	
	ext_suffix = "tar"
	if slug.endswith(ext_suffix):
		slug = slug[:-len(ext_suffix)]	

	slug = slug.replace(".", "_")
	slug = slug.lower()
		
	return slug

'''
	Create thumbnail images
'''
def generate_thumbnail(image, upload_path):
	str_img_data = StringIO(image.read())
	thumb_img = Image.open(str_img_data)
	print "upload_path"
	print upload_path
	# calculate thumb size
	scale = thumb_img.size[0] / float(shotz_settings.SCREENSHOT_THUMB_WIDTH)
	new_size = (int(thumb_img.size[0] / scale), int(thumb_img.size[1] / scale))

	thumb_img.thumbnail(new_size, Image.ANTIALIAS)
	str_img_out = StringIO()

	thumb_img.save(str_img_out, thumb_img.format)

	thumb_name = path.split(image.path)[-1]
	thumb_name = path.splitext(thumb_name)[0] + "_thumb" + path.splitext(thumb_name)[1]

	# prepare to check exist thumb file
	upload_path = settings.MEDIA_ROOT
	#+ upload_path
	print "upload_path"
	print upload_path
	upload_path = path.join(upload_path, thumb_name)
	
	#print "upload_path"
	#print upload_path
	# check and delete exists thumb
	if default_storage.exists(upload_path):
		default_storage.delete(upload_path)

	thumb_dict = {}
	thumb_dict['name'] = thumb_name
	thumb_dict['data'] = str_img_out

	return  thumb_dict
# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import FileModel

from modeltranslation.admin import TranslationAdmin

class FileAdmin(TranslationAdmin):
	# class for adding JqueryUI-based tabbed switches of translarion fields
	class Media:
		js = (
			'/files/modeltranslation/js/force_jquery.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
			'/files/modeltranslation/js/tabbed_translation_fields.js',
			)
		css = {
			'screen': ('/files/modeltranslation/css/tabbed_translation_fields.css',),
			}

admin.site.register(FileModel, FileAdmin)
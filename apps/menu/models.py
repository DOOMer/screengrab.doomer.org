# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    base_url = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.name

    def save(self, force_insert=False, force_update=False):
        """
        Re-order all items at from 10 upwards, at intervals of 10.
        This makes it easy to insert new items in the middle of 
        existing items without having to manually shuffle 
        them all around.
        """
        super(Menu, self).save(force_insert, force_update)
        
        current = 10
        for item in MenuItem.objects.filter(menu=self).order_by('order'):
			item.order = current

			if item.link_url.startswith('http://') or item.link_url.startswith('https://'):
				item.external_url = 1
			else:
				item.external_url = 0

			item.save()			
			current += 10

	class Meta:
		verbose_name = _('Menu')
		verbose_name_plural = _('Menus')

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    order = models.IntegerField()
    link_url = models.CharField(max_length=128, help_text='URL or URI to the content, eg /about/ or http://foo.com/')
    title = models.CharField(max_length=100)
    login_required = models.BooleanField(blank=True)    
    
    # added by me
    target_blank = models.BooleanField(blank=True)
    external_url = models.BooleanField()#editable = False
    
    def __unicode__(self):
        return "%s %s. %s" % (self.menu.slug, self.order, self.title)

	class Meta:
		verbose_name = _('Menu item')
		verbose_name_plural = _('Menus items')		

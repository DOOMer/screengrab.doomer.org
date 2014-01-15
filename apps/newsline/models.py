# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class NewsLine(models.Model):
    pub_date = models.DateTimeField()
    text = models.TextField()
    
    def __unicode__(self):
        return u"%s -- %s" % (self.pub_date, self.text)
    
    class Meta:
        ordering = ('-pub_date',)
        verbose_name = u'Nwesline'
        verbose_name_plural = u'Nweslines' 
    
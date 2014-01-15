# -*- encoding: utf-8 -*-

from django.contrib import admin
from menu.models import Menu, MenuItem

from modeltranslation.admin import TranslationAdmin, TranslationGenericStackedInline

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    readonly_fields = ('external_url',)

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]

# trans
class TranslatedMenuItemeInline(MenuItemInline, TranslationGenericStackedInline):
    model = MenuItem    

class TranslatedMenuAdmin(MenuAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(TranslatedMenuAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

    inlines = [TranslatedMenuItemeInline,]

    
admin.site.register(Menu, MenuAdmin)


#class MenuItemInline(admin.TabularInline):
#    model = MenuItem

#class MenuAdmin(admin.ModelAdmin):
    #inlines = [MenuItemInline,]

#admin.site.register(Menu, MenuAdmin)

from modeltranslation.translator import translator, TranslationOptions

from models import MenuItem

class MenuItemTranslationOptions(TranslationOptions):
	fields = ('title', )

# register our translated models
translator.register(MenuItem, MenuItemTranslationOptions)
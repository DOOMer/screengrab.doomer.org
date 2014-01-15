from modeltranslation.translator import translator, TranslationOptions

# import our models for translating
from models import Page

class PageTranslationOptions(TranslationOptions):
	fields = ('title', 'content', 'meta_description', 'meta_keywords',)
	
# register our translated models
translator.register(Page, PageTranslationOptions)


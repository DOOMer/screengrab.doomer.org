from modeltranslation.translator import translator, TranslationOptions

from apps.newsline.models import NewsLine

class NewsLineTranslationOptions(TranslationOptions):
    fields = ('text', )
	
# register our translated models
translator.register(NewsLine, NewsLineTranslationOptions)

from modeltranslation.translator import translator, TranslationOptions

# import our models for translating
from apps.pages.models import Page
from apps.menu.models import MenuItem
from apps.newsline.models import NewsLine
from apps.filez.models import FileModel
from apps.shotz.models import ScreenshotModel

class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'meta_description', 'meta_keywords',)
    
class MenuItemTranslationOptions(TranslationOptions):
	fields = ('title', )

class NewsLineTranslationOptions(TranslationOptions):
    fields = ('text', )

class FileTranslationOptions(TranslationOptions):
	fields = ('title', )
	
class ScreenshotTranslationOptions(TranslationOptions):
	fields = ('description', )
	
# register our translated models
translator.register(MenuItem, MenuItemTranslationOptions)
translator.register(Page, PageTranslationOptions)
translator.register(NewsLine, NewsLineTranslationOptions)
translator.register(FileModel, FileTranslationOptions)
translator.register(ScreenshotModel, ScreenshotTranslationOptions)

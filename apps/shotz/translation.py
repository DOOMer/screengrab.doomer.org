from modeltranslation.translator import translator, TranslationOptions

# import our models for translating
from models import ScreenshotModel

class ScreenshotTranslationOptions(TranslationOptions):
	fields = ('description', )
	
# register our translated models
translator.register(ScreenshotModel, ScreenshotTranslationOptions)

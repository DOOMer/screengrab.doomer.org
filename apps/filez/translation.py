from modeltranslation.translator import translator, TranslationOptions

# import our models for translating
from apps.filez.models import FileModel

class FileTranslationOptions(TranslationOptions):
	fields = ('title', )
	
# register our translated models
translator.register(FileModel, FileTranslationOptions)
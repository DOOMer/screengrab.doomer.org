from django.conf import settings # import the settings file

#def admin_media(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    #return {'ADMIN_MEDIA_URL': settings.META_DESCRIPTION}

def meta_description(context):
	return {'META_DESCRIPTION': settings.META_DESCRIPTION}
	
def meta_keywords(context):
	return {'META_KEYWORDS': settings.META_KEYWORDS}
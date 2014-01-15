# -*- encoding: utf-8 -*-

# Django settings for screengrab project.

from os import path
import os
import sys

PROJECT_ROOT = path.dirname(__file__)

#Добавляем apps в системную переменную path  
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))  

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('DOOMer', 'doomer3d@gmail.com'),
)

MANAGERS = ADMINS

# saving messages in sessions
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DATABASE_NAME = os.path.join(os.path.dirname(PROJECT_ROOT), os.path.join('db', "screengrab.dbx"))
#= PROJECT_ROOT + '/screengrab.dbx'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DATABASE_NAME,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# meta description
META_DESCRIPTION = "Screengrab - crossplatformapllicationforget screenshots"

#meta keywords
META_KEYWORDS = "screenmgrab,screenshot, application"

# Languages settings for django-modeltranslation app_directories
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

LOCALE_PATHS = (
    PROJECT_ROOT + "/locale",
)

# set default language
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

MODELTRANSLATION_TRANSLATION_FILES = (
    'apps.filez.translation',
    'apps.menu.translation',
	'apps.newsline.translation',
	'apps.pages.translation',
	'apps.shotz.translation',
)

# locale ul independent paths
LOCALE_INDEPENDENT_PATHS = (
   r'^/robots.txt',
#r'^/ajax/',
)

# disable language prefix for default language in urls
PREFIX_DEFAULT_LOCALE = False

DATE_FORMAT = "d E Y"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# debug site url
SITE_URL = "http://localhost:8000"
  
#URL к статическим файлам  
STATIC_URL = '/files/' # profuction 
#STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), os.path.join('files', STATIC_URL.strip('/') ))
#STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_ROOT), STATIC_URL.strip('/') )
STATIC_ROOT = '/home/doomer/web/screengrab/files'

#URL к медиа файлам  
MEDIA_URL = STATIC_URL + 'content/'  
#путь в системе к медиа файлам  
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'content') 
#print STATIC_ROOT
#print MEDIA_ROOT

SCREENSHOT_THUMB_WIDTH = 640

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/files/admin/' # deprecated in 1.4
CKEDITOR_MEDIA_PREFIX = "/files/ckeditor/"
CKEDITOR_UPLOAD_PATH = "/home/doomer/web/screengrab.doomer.org/files/media"
CKEDITOR_MEDIA_URL = "http://vk.com.uz/"
#CKEDITOR_UPLOAD_PATH = MEDIA_ROOT

CKEDITOR_CONFIGS = {
    'default': {        
        'toolbar': 'Basic',
        'height': 300,
        'width': 300,
    },
    'awesome_ckeditor': {
        #'toolbar': 'Full',
        #'height': 300,
        #'width': 600,

        'toolbar': [
            [
                'Source','Undo', 'Redo',
                '-', 'Bold', 'Italic', 'Underline', 'Strike', 
                '-', 'BulletedList', 'NumberedList', 
                '-','Blockquote','-','JustifyLeft','JustifyCenter','JustifyRight',
                '-', 'Image', 'Link', 'Unlink', 'Anchor', 'HorizontalRule',                          
                '-', 'Maximize',
            ],
        ],
        'width': 840,
        'height': 300,
        'toolbarCanCollapse': False,
    },
}

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gc7d@8h%tuvu&o9$840u+q^(4ml(*wxa5j80jn-x&t8p1e_xl@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# list of template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static", 
#    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
	"django.contrib.messages.context_processors.messages", 
    
    # feedbak context processor
    "feedback_form.context_processors.meta_description",
    "feedback_form.context_processors.meta_keywords",
)

MIDDLEWARE_CLASSES = (
	# middleware for localurl app_directories
	'localeurl.middleware.LocaleURLMiddleware', 
	
	# default middlewares
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
	path.join(PROJECT_ROOT, 'tpl').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#CONTACT_ADMINS_ONLY = False
CONTACT_SEND_META_INFO = True

#SESSION_COOKIE_DOMAIN = 'screengrab.doomer.org'
#CSRF_COOKIE_DOMAIN = 'screengrab.doomer.org'
#LANGUAGE_COOKIE_NAME = 'screengrab_lang'

INSTALLED_APPS = (
	# localuel app
	 'localeurl',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    
    # 3rd party apps
    'modeltranslation',
    
    # my apss
    'apps.pages', 
    'apps.menu',  
    'apps.feedback_form',
    'apps.ckeditor', 
    'apps.newsline',
	'apps.filez',
	'apps.shotz',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#ALLOWED_HOSTS = [
#    'screengrab.doomer.org',
#    '62.113.232.71',
#]
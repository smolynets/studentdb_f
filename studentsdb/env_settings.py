SECRET_KEY = 'g$@n#h!a6!b&5-@16to05z3s%&#^c@xp3f@^v849_#nwq&fzoj'


#dont DEBUG
#DEBUG = True
#TEMPLATE_DEBUG = True
DEBUG = False
TEMPLATE_DEBUG = False


ALLOWED_HOSTS = ['students.vitaliypodoba.com', 'demo-students.vitaliypodoba.com']

#ALLOWED_HOSTS = []


PORTAL_URL = 'http://students.vitaliypodoba.com'



DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'HOST': 'localhost',
      'USER': 'students_db_user',
      'PASSWORD': 'Xa6o5Tit3W',
      'NAME': 'students_db',
    }
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'smolynets1@gmail.com'
EMAIL_HOST_PASSWORD = 'dobrosyno'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'





# static files
STATIC_URL = '/static/'
STATIC_ROOT = '/home/oleh/virt/studentsdb/src/media'




# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/to/folder/with/media/files/'


# facebook API Keys
SOCIAL_AUTH_FACEBOOK_KEY = '1217953244967675'
SOCIAL_AUTH_FACEBOOK_SECRET = '62fbef0a464deec462f279efc1a7'





# admins
ADMINS = (('Oleh', 'oleh.smolynets@gmail.com'),)
MANAGERS = (('Manager', 'oleh.smolynets@gmail.com' ),)





# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    # }
   # 'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
     #   'NAME': 'mydb1',
      #  'USER': 'oleh1',
       # 'PASSWORD': '0000',
       # 'HOST': 'localhost',
       # 'PORT': '',
    #}
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'HOST': 'localhost',
      'USER': 'students_db_user',
      'PASSWORD': '0000',
      'NAME': 'students_db',
    }
}

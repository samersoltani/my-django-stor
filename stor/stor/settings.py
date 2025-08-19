# stor/stor/settings.py

import os
from pathlib import Path
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'django-insecure-a-default-key-for-your-computer'
)

DEBUG = os.environ.get('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'core',
    'account',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.middleware.messages',
                'cart.context_processors.cart',
                 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stor.wsgi.application'


# ==============================================================================
# DATABASE 
# ==============================================================================

# اگر روی سرور اجرا شود (یعنی DATABASE_URL وجود داشته باشد)، از آن استفاده می‌کند
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)
    }
else:
    # اگر روی کامپیوتر شما اجرا شود، از این دیتابیس SQLite استفاده می‌کند
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
# ==============================================================================
# PASSWORD VALIDATION, INTERNATIONALIZATION, ETC.
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# STATIC & MEDIA FILES
# ==============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STORAGES = {
    "default": { "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage" },
    "staticfiles": { "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage" },
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# ==============================================================================
# CUSTOM SETTINGS
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CART_SESSION_ID = 'cart'
AUTH_USER_MODEL = 'account.CustomUser'
LOGOUT_REDIRECT_URL = 'core:home'


# تنظیمات درگاه پرداخت (برای مثال)

SANDBOX = True

MERCHANT = '00000000-0000-0000-0000-000000000000'



# تنظیمات ایمیل

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'noreply@my-shop.com'

ADMIN_EMAIL = 'your-email@example.com'





# Django settings for stor project.


# import os

# from pathlib import Path

# import dj_database_url



# # Build paths inside the project like this: BASE_DIR / 'subdir'.

# BASE_DIR = Path(__file__).resolve().parent.parent





# # ==============================================================================

# # CORE SETTINGS

# # ==============================================================================



# # SECURITY WARNING: keep the secret key used in production secret!

# # این کلید باید در متغیرهای محیطی Render تنظیم شود

# SECRET_KEY = os.environ.get('SECRET_KEY')



# # SECURITY WARNING: don't run with debug turned on in production!

# # در محیط آنلاین، دیباگ همیشه باید خاموش باشد

# DEBUG = False



# # تنظیمات پیشرفته و امن برای هاست‌های مجاز

# ALLOWED_HOSTS = []

# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

# if RENDER_EXTERNAL_HOSTNAME:

#     ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)



# # برای اطمینان، دامنه اصلی را هم به صورت دستی اضافه می‌کنیم

# ALLOWED_HOSTS.append('my-django-store.onrender.com')

# # ALLOWED_HOSTS = [

# #     'naıkestor.onrender.com',  # آدرس سرویس شما در رانفلر

# #     'my-django-store.onrender.com',  # آدرس سرویس شما در رندر

# # ]



# # ==============================================================================

# # APPLICATION DEFINITION

# # ==============================================================================



# INSTALLED_APPS = [

#     # اپلیکیشن‌های جنگو

#     'django.contrib.admin',

#     'django.contrib.auth',

#     'django.contrib.contenttypes',

#     'django.contrib.sessions',

#     'django.contrib.messages',

#     'django.contrib.staticfiles',



#     # اپلیکیشن‌های شخص ثالث (Third-Party)

#     'cloudinary',

#     'cloudinary_storage',

#    

#     # اپلیکیشن‌های شما (My Apps)

#     'core',

#     'account',

#     'cart',

# ]



# MIDDLEWARE = [

#     'django.middleware.security.SecurityMiddleware',

#     # WhiteNoise باید دقیقاً بعد از SecurityMiddleware باشد

#     'whitenoise.middleware.WhiteNoiseMiddleware',

#     'django.contrib.sessions.middleware.SessionMiddleware',

#     'django.middleware.common.CommonMiddleware',

#     'django.middleware.csrf.CsrfViewMiddleware',

#     'django.contrib.auth.middleware.AuthenticationMiddleware',

#     'django.contrib.messages.middleware.MessageMiddleware',

#     'django.middleware.clickjacking.XFrameOptionsMiddleware',

# ]



# ROOT_URLCONF = 'stor.urls'



# TEMPLATES = [

#     {

#         'BACKEND': 'django.template.backends.django.DjangoTemplates',

#         'DIRS': [os.path.join(BASE_DIR, 'templates')], # مسیر عمومی تمپلیت‌ها

#         'APP_DIRS': True,

#         'OPTIONS': {

#             'context_processors': [

#                 'django.template.context_processors.request',

#                 'django.contrib.auth.context_processors.auth',

#                 'django.contrib.messages.context_processors.messages',

#                 'cart.context_processors.cart',

#             ],

#         },

#     },

# ]



# WSGI_APPLICATION = 'stor.wsgi.application'





# # ==============================================================================

# # DATABASE

# # ==============================================================================



# DATABASES = {

#     'default': dj_database_url.config(

#         # این خط به صورت خودکار متغیر DATABASE_URL را از Render می‌خواند

#         default=os.environ.get('DATABASE_URL'),

#         conn_max_age=600,

#         ssl_require=True # این گزینه برای اتصال امن در Render مهم است

#     )

# }



# # اگر برنامه روی Render اجرا شود، از دیتابیس آنلاین PostgreSQL استفاده می‌کند

# # ssl_require=True برای امنیت بیشتر در اتصال به دیتابیس Render اضافه شده است

# if 'DATABASE_URL' in os.environ:

#     DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)





# # ==============================================================================

# # PASSWORD VALIDATION

# # ==============================================================================



# AUTH_PASSWORD_VALIDATORS = [

#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},

#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},

#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},

#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},

# ]





# # ==============================================================================

# # INTERNATIONALIZATION

# # ==============================================================================



# LANGUAGE_CODE = 'fa-ir'

# TIME_ZONE = 'Asia/Tehran'

# USE_I18N = True

# USE_TZ = True





# # ==============================================================================

# # STATIC & MEDIA FILES

# # ==============================================================================



# # تنظیمات مربوط به فایل‌های استاتیک (CSS, JavaScript)

# STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# # تنظیمات مربوط به فایل‌های آپلود شده توسط کاربر (Media)

# # این دو خط باید وجود داشته باشند اما در حالت Cloudinary، جنگو از آنها استفاده مستقیم نمی‌کند

# MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# # تنظیمات برای اتصال به Cloudinary

# # این بخش به جنگو می‌گوید که تمام فایل‌ها را در Cloudinary مدیریت کند

# CLOUDINARY_STORAGE = {

#     'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),

#     'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),

#     'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),

# }

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'





# # ==============================================================================

# # CUSTOM SETTINGS

# # ==============================================================================



# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CART_SESSION_ID = 'cart'

# AUTH_USER_MODEL = 'account.CustomUser'

# LOGOUT_REDIRECT_URL = 'core:home' # بهتر است از namespace استفاده شود



# # تنظیمات درگاه پرداخت (برای مثال)

# SANDBOX = True

# MERCHANT = '00000000-0000-0000-0000-000000000000'



# # تنظیمات ایمیل

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEFAULT_FROM_EMAIL = 'noreply@my-shop.com'

# ADMIN_EMAIL = 'your-email@example.com'


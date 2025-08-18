# stor/stor/settings.py

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

# کلید مخفی به صورت امن از متغیرهای محیطی خوانده می‌شود
# و یک مقدار پیش‌فرض برای محیط توسعه دارد.
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'django-insecure-your-default-development-key' # یک کلید پیش‌فرض برای کامپیوتر شما
)

# حالت دیباگ به صورت هوشمند از متغیرهای محیطی خوانده می‌شود.
# در سرور Render (که این متغیر وجود ندارد) به صورت خودکار False خواهد بود.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# تنظیمات امن و هوشمند برای هاست‌های مجاز
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise باید اینجا باشد
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
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'stor.wsgi.application'

# ==============================================================================
# DATABASE (بخش اصلاح‌شده و بسیار مهم)
# ==============================================================================

DATABASES = {
    'default': dj_database_url.config(
        # اگر روی کامپیوتر شما اجرا شود، از این دیتابیس SQLite استفاده می‌کند
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        # اگر روی سرور اجرا شود، متغیر DATABASE_URL را می‌خواند
        conn_max_age=600
    )
}

# ==============================================================================
# PASSWORD VALIDATION
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================================================================
# INTERNATIONALIZATION
# ==============================================================================

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
# نکته: MEDIA_ROOT در حالت Cloudinary استفاده نمی‌شود، اما تعریف آن ضرری ندارد
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# تنظیمات جدید و استاندارد برای ذخیره‌سازی فایل‌ها
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# تنظیمات اتصال به Cloudinary
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
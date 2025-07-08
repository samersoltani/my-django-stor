"""
URL configuration for stor project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    
    # این تنها کد مورد نیاز برای نمایش فایل‌های Media در محیط آنلاین است
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
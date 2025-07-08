"""
URL configuration for stor project.
"""
from django.contrib import admin
from django.urls import path, include ,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# این خط برای نمایش تصاویر آپلودی (media) در محیط آنلاین ضروری است
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),

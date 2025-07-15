from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
]
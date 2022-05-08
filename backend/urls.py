from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('Cities.urls')),
    path('api/v1/', include('Foods.urls')),
    path('api/v1/', include('CostOfLiving.urls')),
    path('api/v1/', include('Transport.urls')),
    path('api/v1/', include('Language.urls')),
    path('api/v1/', include('Apps.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

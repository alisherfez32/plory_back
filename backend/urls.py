from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Stepbook'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('Test.urls')),
    path('api/v1/', include('Cities.urls')),
    path('api/v1/', include('Foods.urls')),
    path('api/v1/', include('CostOfLiving.urls')),
    path('api/v1/', include('Transport.urls')),
    path('api/v1/', include('Language.urls')),
    path('api/v1/', include('Apps.urls')),
    path('api/v1/', include('Score.urls')),
    path('api/v1/', include('Visit.urls')),
    path('api/v1/', include('Rent.urls')),
    path('api/v1/', include('IMAGES.urls')),
    path('api/v1/', include('Search.urls')),
    path('api/v1/', include('EatPlace.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

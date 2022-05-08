from django.urls import path

from . import views

urlpatterns = [
    path('apps/', views.ListApps.as_view()),
    path('apps/country/', views.Apps.as_view()),
    path('apps/country/<slug:country_slug>/', views.CountryWithApps.as_view()),
]
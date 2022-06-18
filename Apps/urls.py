from django.urls import path

from . import views

urlpatterns = [
    path('apps/', views.ListApps.as_view()),
    path('apps/country/<slug:country_slug>/', views.CountryWithApps.as_view()),

    path('apps/list_filters/', views.ListFilter().as_view()),
    path('apps/filter_by/', views.filter_by)
]
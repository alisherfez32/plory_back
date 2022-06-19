from django.urls import path

from . import views

urlpatterns = [
    path('images/', views.AllImages.as_view()),
    path('images/list_filters/', views.ListFilter.as_view()),
    path('images/<slug:country_slug>/', views.CountryImages.as_view()),
    path('images/city/<slug:city_slug>/', views.CityImages.as_view()),
    path('images/filter_by/<slug:city_slug>/', views.filter_by),
    path('images/filter_by/country/<slug:country_slug>/', views.filter_by_country),
]

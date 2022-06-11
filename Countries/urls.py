from django.urls import path
from . import views

urlpatterns = [
    path('country-tree/', views.CountyWithCities.as_view()),
    path('country-tree/<slug:country_slug>/', views.CountryDetail.as_view()),
    path('city-tree/detailed/<slug:country_slug>/', views.CountryCityDetailed.as_view()),  # List cities with Slug of country

]

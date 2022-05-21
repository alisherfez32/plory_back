from django.urls import path, include
from . import views

urlpatterns = [
    path('continent-tree/', views.ListContinents.as_view()),
    path('country-tree/', views.CountyWithCities.as_view()),
    path('country-tree/<slug:country_slug>/', views.CountryDetail.as_view()),
    path('city-tree/', views.ListCities.as_view()),
    path('city-tree/detailed/', views.ListCityDetails.as_view()),
    path('city-tree/detailed/<slug:country_slug>/', views.CountryCityDetailed.as_view()),
    path('city-tree/detailed/info/<str:city_slug>/', views.CityDetailed.as_view()),
]
from django.urls import path
from . import views

urlpatterns = [
    path('continent-tree/', views.ListContinents.as_view()),
    path('city-tree/', views.ListCities.as_view()),
    # Detailed Everything
    path('city-info/', views.ListCityDetails.as_view()),
    path('city-info/<str:city_slug>/', views.CityDetailed.as_view()),
    # Get city by country
    # path('city-tree/detailed/<slug:country_slug>/', views.CountryCityDetailed.as_view()),
]
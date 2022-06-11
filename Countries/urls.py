from django.urls import path
from . import views

urlpatterns = [
    path('country-tree/', views.CountyWithCities.as_view()),
    path('country-info/', views.CountryInfo.as_view()),
    path('country-tree/<slug:country_slug>/', views.CountryDetail.as_view()),

]

from django.urls import path

from . import views

urlpatterns = [
    path('images/', views.AllImages.as_view()),
    path('images/<slug:country_slug>/', views.CountryImages.as_view()),
    path('images/city/<slug:city_slug>/', views.CityImages.as_view()),
]

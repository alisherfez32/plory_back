from django.urls import path
from . import views

urlpatterns = [
    path('continent-tree/', views.ListContinents.as_view()),
    path('city-tree/', views.ListCities.as_view()),
    # Detailed Everything
    path('city-tree/detailed/', views.ListCityDetails.as_view()),
    path('city-tree/detailed/info/<str:city_slug>/', views.CityDetailed.as_view()),
]
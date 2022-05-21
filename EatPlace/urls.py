from django.urls import path

from . import views

urlpatterns = [
    path('eats/', views.ListOfEats.as_view()),
    path('eats/city/<slug:city_slug>/', views.CityEats.as_view()),
]

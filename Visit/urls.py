from django.urls import path

from . import views

urlpatterns = [
    path('visits/', views.ListVisits.as_view()),
    path('visits/city/<slug:city_slug>/', views.CityVisits.as_view()),
]

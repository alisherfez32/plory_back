from django.urls import path

from . import views

urlpatterns = [
    path('scores/', views.ListScores.as_view()),
    path('scores/city/<slug:city_slug>/', views.CityScores.as_view()),
]
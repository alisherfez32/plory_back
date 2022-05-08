from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.ListOfFoods.as_view()),
    path('foods/country/<str:country_slug>/', views.CountryListFood.as_view()),
]
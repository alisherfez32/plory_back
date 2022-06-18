from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.ListOfFoods.as_view()),
    path('foods/country/<str:country_slug>/', views.CountryListFood.as_view()),
    path('foods/list_filters/', views.ListFilter().as_view()),
    path('foods/filter_by/', views.filter_by)
]
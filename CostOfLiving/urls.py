from django.urls import path
from . import views

urlpatterns = [
    path('costs/', views.ListCostOfLiving.as_view()),
    path('costs/city/<slug:city_slug>/', views.CountryCostOfLiving.as_view()),
]
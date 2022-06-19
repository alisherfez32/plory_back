from django.urls import path
from . import views

urlpatterns = [
    path('costs/', views.ListCostOfLiving.as_view()),
    path('costs/city/<slug:city_slug>/', views.CityCosts.as_view()),
    path('costs/list_filters/', views.ListFilter.as_view()),
    path('costs/filter_by/', views.filter_by),
]
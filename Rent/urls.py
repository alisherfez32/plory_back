from django.urls import path

from . import views

urlpatterns = [
    path('rents/', views.ListRents.as_view()),
    path('rents/city/<slug:city_slug>/', views.CityRents.as_view()),
    path('rents/list_filters/', views.ListFilter.as_view()),
    path('rents/filter_by/', views.filter_by)
]

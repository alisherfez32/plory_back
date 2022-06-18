from django.urls import path
from . import views

urlpatterns = [
    path('transports/', views.ListTransports.as_view()),
    path('transports/country/<slug:country_slug>/', views.CountryTransports.as_view()),
    path('transports/list_filters/', views.ListFilter().as_view()),
    path('transports/filter_by/', views.filter_by)
]
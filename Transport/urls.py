from django.urls import path
from . import views

urlpatterns = [
    path('transports/', views.ListTransports.as_view()),
    path('transports/country/<slug:country_slug>/', views.CountryTransports.as_view()),
]
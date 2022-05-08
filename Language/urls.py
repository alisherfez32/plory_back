from django.urls import path

from . import views

urlpatterns = [
    path('languages/', views.ListLanguages.as_view()),
]
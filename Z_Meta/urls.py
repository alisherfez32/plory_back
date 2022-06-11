from django.urls import path
from . import views

urlpatterns = [
    path('meta/', views.Meta.as_view()),
    path('meta/<slug:component>/', views.MetaComponent.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.urlshortener, name="url-shortener"),
]

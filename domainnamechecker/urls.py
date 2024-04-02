from django.urls import path
from . import views

urlpatterns = [
    path('',views.domain_search, name="domain-search"),
    
    
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('domain-search/', include('domainnamechecker.urls')),
    path('task-manager/', include('taskmanager.urls')),   
    path('url-shortener/', include('urlshortener.urls')),   
    path('image-resizer/', include('imageresizer.urls')),
    path('text-summarizer/', include('textsummarizer.urls')),
]

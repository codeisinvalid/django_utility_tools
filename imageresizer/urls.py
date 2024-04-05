from django.urls import path
from . import views

urlpatterns = [
    path('',views.image_resizer, name="image-resizer"),
    path('editor/', views.image_editor, name='image_editor'),

]

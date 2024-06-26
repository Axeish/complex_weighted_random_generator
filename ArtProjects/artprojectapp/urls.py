from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_project/', views.add_project, name='add_project'),
]

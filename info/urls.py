from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.about),
    path('', views.about, name='home-link'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='meqale-link'),
    path('post', views.post, name='single-meqale')
]
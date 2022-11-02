from urllib import request
from django.urls import path
from recipes import views


urlpatterns = [
    path('' , views.home),
    path('dia/', views.dia),
]
from django.contrib import admin
from django.urls import path
from manager_login import views

urlpatterns = [
    path('login/',views.index),
   # path('Manger_login/',include('manger_login.urls')),
]

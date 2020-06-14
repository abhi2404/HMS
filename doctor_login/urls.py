from django.contrib import admin
from django.urls import path
from doctor_login import views
from .views import signup , dr_login

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.dr_login,name="dr_login")
]
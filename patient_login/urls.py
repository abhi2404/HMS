from django.contrib import admin
from django.urls import path
from patient_login import views
from .views import signup , pt_login

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.pt_login,name="pt_login")
    ]
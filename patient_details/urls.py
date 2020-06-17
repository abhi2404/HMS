from django.contrib import admin
from django.urls import path
from patient_details import views
from .views import apt , medical_history

urlpatterns = [
    path('appointment/',views.apt,name="appointment"),
    path('appointment/details/',views.display_apt,name="appointment details"),
    path('appointment/medical_history/',views.medical_history,name="medical_history"),
    path('appointment/medical_history/display/',views.display_history,name="display_history"),

   
]
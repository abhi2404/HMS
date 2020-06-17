from django.contrib import admin
from django.urls import path
from manager_login import views
from .views import index,dr_registration, registration_accept,registration_reject,registration_approved,registration_disapproved

urlpatterns = [
    path('login/',views.index,name="login"),
    path('doctor_registration/',views.dr_registration,name="doctor_registration"),
    path('doctor_registration/accept/',views.registration_accept,name="registration_accept"),
    path('doctor_registration/reject/',views.registration_reject,name="registration_reject"),
    path('doctor_registration/accept/list/',views.registration_approved,name="approved_registration"),
    path('doctor_registration/reject/list/',views.registration_disapproved,name="disapproved_registration"),
]

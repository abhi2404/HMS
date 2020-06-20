from django.urls import path
from doctor_dashboard import views
from .views import show_appointment_doctor,show_appointment_id,appointment_accept,modify_appointment,show_appointment_confirm,report,count
urlpatterns = [
    path('appointment/',views. show_appointment_doctor,name="appointment"),
    path('appointment/details/',views. show_appointment_id,name="appointment_details"),
    path('appointment/accept/',views.appointment_accept,name="appointment_accept"),
    path('appointment/modify/',views.modify_appointment,name="appointment_modify"),
    path('appointment/confirm_list/',views.show_appointment_confirm,name="confirm_list_appointment"),
    path('medical_history/',views.show_medical_history,name="modical-history"),
    path('report/',views.report,name="report"),
    path('count/',views.count,name="count"),
]
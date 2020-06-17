from django.urls import path
from manager_dashboard import views
from .views import show_details , show_appointment , show_appointment_id,send_doctor_list, forward_appointment , reject_appointment

urlpatterns = [
    path('show_details/',views.show_details,name="patient_details"),
    path('show_appointment/',views.show_appointment,name="patient_appointment"),
    path('show_appointment/id/',views.show_appointment_id,name="patient_appointment_id"),
    path('field/doctor_list/',views.send_doctor_list,name="doctor_list"),
    path('appointment_forward/',views.forward_appointment,name="appointment_forward"),
    path('appointment_reject/',views.reject_appointment,name="reject_forward")
]
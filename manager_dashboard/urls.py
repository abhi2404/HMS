from django.urls import path
from manager_dashboard import views
from .views import show_details , show_appointment , show_appointment_id,send_doctor_list, forward_appointment , reject_appointment,confirm_appointment,modify_confirm_appointment,bill_payment,show_payment_details,show_payment_fees

urlpatterns = [
    path('show_details/',views.show_details,name="patient_details"),
    path('show_appointment/',views.show_appointment,name="patient_appointment"),
    path('show_appointment/id/',views.show_appointment_id,name="patient_appointment_id"),
    path('field/doctor_list/',views.send_doctor_list,name="doctor_list"),
    path('appointment_forward/',views.forward_appointment,name="appointment_forward"),
    path('appointment_reject/',views.reject_appointment,name="reject_forward"),
    path('appointment_confirm/',views.confirm_appointment,name="confirm_forward"),
    path('modify_appointment_confirm/',views.modify_confirm_appointment,name="modify_confirm_forward"),
    path('payment/',views.bill_payment,name="payment"),
    path('payment_show/',views.show_payment_details,name="payment_show"),
    path('payment_fees/',views.show_payment_fees,name="payment_fees"),
]
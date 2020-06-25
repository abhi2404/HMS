from django.contrib import admin
from django.urls import path
from patient_details import views
from .views import apt , medical_history,test_cost,prescription,detail_report,notification,remove

urlpatterns = [
    path('appointment/',views.apt,name="appointment"),
    path('appointment/details/',views.display_apt,name="appointment details"),
    path('appointment/medical_history/',views.medical_history,name="medical_history"),
    path('appointment/medical_history/display/',views.display_history,name="display_history"),
    path('show_fees/',views.show_fees,name="show_fees"),
    path('test_cost/',views.test_cost,name="test_cost"),
    path('report_date/',views.prescription,name="report_date"),
    path('report_details/',views.detail_report,name="report_details"),
    path('notification/',views.notification,name="notification"),
    path('notification/cancel/',views.remove,name="remove_notification")
]
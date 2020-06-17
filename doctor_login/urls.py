from django.urls import path
from doctor_login import views
from .views import signup , dr_login,degree,field

urlpatterns = [
    path('field/',views.field,name="field"),
    path('degree/',views.degree,name="degree"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.dr_login,name="dr_login")
]
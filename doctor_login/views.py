from django.shortcuts import render,HttpResponse
import json 
from django.http import JsonResponse
from .models import doctor_login

# Create your views here.
def signup(request):
	if request.method =="POST":
		print(request.body)
		data=json.loads(request.body)
		name=data['name']
		username=data['email']
		password=data['password']
		doctor_degree=data['degree']
		mobile_no=data['contact_no']
		unique_email=doctor_login.objects.filter(email=username).exists()
		if(unique_email):
			message ="This email is already registered"
		else:
			doctor_login.objects.create(name=name,email=username,password=password,doctor_degree=doctor_degree,mobile_no=mobile_no)
			message="pending"
	return JsonResponse(message,safe=False)

		

def dr_login(request):
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=doctor_login.objects.filter(email=username,password=password,status="confirmed").exists()  
		print(bool_filter)
		if (bool_filter):
			message="ok"
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)

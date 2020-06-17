from django.shortcuts import render,HttpResponse
import json 
from django.http import JsonResponse
from .models import doctor_login , doctor_degree,specialization

# Create your views here.
def signup(request):
	if request.method =="POST":
		print(request.body)
		data=json.loads(request.body)
		name=data['name']
		username=data['email']
		password=data['password']
		doctor_degree=data['degree']
		field=data['field']
		mobile_no=data['contact_no']
		unique_email=doctor_login.objects.filter(email=username).exists()
		if(unique_email):
			message ="This email is already registered"
		else:
			doctor_login.objects.create(name=name,email=username,password=password,doctor_degree=doctor_degree,mobile_no=mobile_no,field=field)
			message="pending"
	return JsonResponse(message,safe=False)

		

def dr_login(request):
	if request.method == "POST":
		print(request.body)
		data=json.loads(request.body)
		username=data['email']
		password=data['password']
		bool_filter=doctor_login.objects.filter(email__contains=username,password__contains=password,status="confirmed").exists()  
		print(bool_filter)
		if (bool_filter):
			message="ok"
		else:
			message="invalid credentials"	
	return JsonResponse(message,safe=False)

def degree(request):
	if request.method == "GET":
		message=doctor_degree.objects.values()
	return JsonResponse(list(message),safe=False)
 
def field(request):
    if request.method =="GET":
    	print(request)
    	data=request.GET.get('degree')
    	print(data)
    	filter_degree=doctor_degree.objects.filter(degree=data)
    	for degree in filter_degree:
    		Id=degree.id
    		print(Id)
    		message=specialization.objects.filter(link_id=Id).values('field')
    		break
    return JsonResponse(list(message),safe=False)
	

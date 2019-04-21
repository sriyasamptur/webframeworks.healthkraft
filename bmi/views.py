from django.http import HttpResponse
from django import forms
from django.shortcuts import render
def form_print(request):
	return render(request, 'firstform.html', {})
 
def form_get(request):
	height=request.POST.get('height','')
	weight=request.POST.get('weight','')
	weight=float(weight)
	height=float(height)
	BMI = weight/(height*height)
	 
	weight=str(weight)
	height=str(height)
	BMI=str(BMI)
	return render(request, 'firstform1.html', {'text':"Your Height =" + height + "meter" + "Your Weight =" + weight + "KG"  +  "Your BMI =" + BMI })
	#return HttpResponse("Your Height =" + height + "meter" + "Your Weight =" + weight + "KG  +  Your BMI =" + BMI )

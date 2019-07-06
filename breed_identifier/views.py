from django.shortcuts import render

def home(request):
	return render(request, 'breed_identifier/home.html')

def about(request):
	return render(request, 'breed_identifier/about.html')
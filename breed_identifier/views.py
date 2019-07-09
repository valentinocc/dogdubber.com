from django.shortcuts import render
from .forms import PictureUploadForm

def home(request):
	picture_form = PictureUploadForm()

	context = {
		'picture_form' : picture_form
	}

	return render(request, 'breed_identifier/home.html', context)

def about(request):
	return render(request, 'breed_identifier/about.html')
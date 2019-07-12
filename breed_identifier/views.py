from django.shortcuts import render
from .forms import PictureUploadForm
from .test_function import predict_breed
import logging



def home(request):
	logger = logging.getLogger(__name__)

	if request.method == 'POST':
		picture_form = PictureUploadForm(request.POST, request.FILES)

		if picture_form.is_valid():
			breed = predict_breed(request.FILES['image'])

		context = {
		'picture_form' : picture_form,
		'breed' : breed
		}

		print(area)

		return render(request, 'breed_identifier/home.html', context)

	else:
		picture_form = PictureUploadForm()

	context = {
		'picture_form' : picture_form
	}


	return render(request, 'breed_identifier/home.html', context)

def about(request):
	return render(request, 'breed_identifier/about.html')
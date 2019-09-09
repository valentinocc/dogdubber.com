from django.shortcuts import render
from .forms import PictureUploadForm
from .test_function import predict_breed
import logging
from .models import DogPicture



def home(request):
	logger = logging.getLogger(__name__)

	if request.method == 'POST':
		picture_form = PictureUploadForm(request.POST, request.FILES)

		if picture_form.is_valid():
			breed = predict_breed(request.FILES['image'])
			dog_name = request.POST['dog_name']

		context = {
		'picture_form' : picture_form,
		'breed' : breed,
		'display_breed' : True,
		'dog_name': dog_name
		}

		if (request.user.is_authenticated):
			DogPicture.objects.create(user=request.user, dog_name=request.POST['dog_name'], image=request.FILES['image'], breed=breed)

		return render(request, 'breed_identifier/home.html', context)

	else:
		picture_form = PictureUploadForm()

	context = {
		'picture_form' : picture_form,
		'display_breed': False
	}


	return render(request, 'breed_identifier/home.html', context)

def about(request):
	return render(request, 'breed_identifier/about.html')
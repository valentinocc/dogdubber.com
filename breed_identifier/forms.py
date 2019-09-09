from django import forms
from .models import DogPicture

class PictureUploadForm(forms.ModelForm):
	class Meta:
		model = DogPicture
		fields = ['image', 'dog_name']
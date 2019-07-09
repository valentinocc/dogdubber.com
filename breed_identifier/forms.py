from django import forms

class PictureUploadForm(forms.ModelForm):
	class Meta:
		model = DogPicture
		field = ['image']
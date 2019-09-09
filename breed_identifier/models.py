from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class DogPicture(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	dog_name = models.CharField(default="Your dog's name", max_length=30)
	image = models.ImageField(default='default.jpg', upload_to='dog_pics')
	breed = models.CharField(default='Placeholder Breed', max_length=40)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if (img.height > 300 or img.width > 300):
			output_size = (350, 350)
			img.thumbnail(output_size)
			img.save(self.image.path)
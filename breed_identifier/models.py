from django.db import models

# Create your models here.
class Dog_Picture(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='dog_pics')
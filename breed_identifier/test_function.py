import numpy as np
from PIL import Image
import torch
import torch.nn as nn
import torchvision
from torchvision import models
from torchvision.transforms import Compose, CenterCrop, Resize, ToTensor, Normalize
from torch.autograd import Variable

def predict_breed( image ):
	n_class = 120

	image = load_image( image )
	mobilenet = models.mobilenet_v2()
	mobilenet.classifier = nn.Sequential(nn.Dropout(0.2), nn.Linear(mobilenet.last_channel, n_class))
	mobilenet.load_state_dict(torch.load('breed_identifier/mobilenet_model.pth', map_location='cpu'))
	mobilenet.eval()
	output = mobilenet( image )
	prediction = top_prediction( output )

	return prediction

def load_image( image ):
	transforms = Compose([Resize(256), CenterCrop(224), ToTensor(), Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

	image = Image.open( image )
	image = transforms( image ).float()
	image = Variable( image )
	image = image.unsqueeze(0)
	return image

def top_prediction( model_output ):
	values, preds = torch.max( model_output.data, 1 )
	prediction = prediction_to_name( preds )
	prediction = clean_breed_name( prediction )
	return prediction

def prediction_to_name( predictions ):
	#assuming prediction is the top prediction right now
	classes = read_classes()
	return classes[predictions[0]]

def read_classes():
	f = open('breed_identifier/dog_breeds.txt', 'r')
	classes = f.read()
	classes = classes.split(',')
	return classes

#remove numbers and underscores in class names
def clean_breed_name( breed_name ):
	breed_name = breed_name.split('-')[1]
	breed_name = breed_name.replace("_", " ")
	breed_name = breed_name.title()
	return breed_name


from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='breed-identifier-home'),
	path('about/', views.about, name='breed-identifier-about'),
]
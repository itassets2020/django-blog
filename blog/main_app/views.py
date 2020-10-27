from django.shortcuts import render
from django.http import HttpResponse

# Home page
def home(request):
	return HttpResponse('<h1>Blog Home</h1>')

# About page
def about(request):
	return HttpResponse('<h1>Blog About</h1>')
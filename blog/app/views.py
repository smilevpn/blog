from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	return HttpResponse('<h1>Main</h1>')
 
def about(request):
	return HttpResponse('<h1>test</h1>')

# Create your views here.

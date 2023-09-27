from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, "app/index.html", None)
def about(request):
    return HttpResponse('<h1>test</h1>')

# Create your views here.

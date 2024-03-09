from django.shortcuts import redirect, render
from django.views.generic import DetailView

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html", None)

from django.shortcuts import redirect, render

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html", None)

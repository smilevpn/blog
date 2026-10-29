from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView  # новое
from django.http import JsonResponse
from .forms import SubscribeForm
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 5


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detail.html'
    
def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Вы подписались!"}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

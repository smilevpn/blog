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
            return JsonResponse({"message": "Вы успешно подписались!"}, status=201)
        
        # Если форма невалидна, проверяем, не связано ли это с тем, что email уже есть
        if 'email' in form.errors:
            for error in form.errors['email']:
                if "already exists" in error: # Проверяем текст ошибки от Django
                    return JsonResponse({"message": "Вы уже подписаны на рассылку!"}, status=200)
        
        # Если ошибка другая (например, неверный формат email)
        return JsonResponse({"errors": form.errors}, status=400)
        
    return JsonResponse({"error": "Invalid request"}, status=400)
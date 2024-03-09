from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView  # новое

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 5


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detail.html'
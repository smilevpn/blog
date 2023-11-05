from django.views.generic import ListView, DetailView  # новое

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 3


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detail.html'
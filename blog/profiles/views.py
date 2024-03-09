from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from .models import Profile

class ProfileDetail(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "user_detail.html"
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post
# Create your views here.
class news(ListView):
    model = Post
    template_name = "news.html"
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
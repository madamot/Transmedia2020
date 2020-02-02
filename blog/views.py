from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from .models import Blog

# Create your views here.
class BlogListView(ListView):
        model = Blog
        template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

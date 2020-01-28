from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView

from .models import blog

# Create your views here.
class BlogListView(ListView):
        model = blog
        template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = blog
    template_name = 'blog_detail.html'

class IndexView(TemplateView):
    template_name = 'index.html'

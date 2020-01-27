from django.shortcuts import render

from django.views.generic import ListView

from .models import blog

# Create your views here.
class BlogListView(ListView):
        model = blog
        template_name = 'blog.html'

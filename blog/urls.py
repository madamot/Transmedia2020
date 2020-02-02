from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('', BlogListView.as_view(), name='blog'),
]

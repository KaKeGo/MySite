from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Blog
from .forms import BlogCreateForm, BlogUpdateForm

# Create your views here.


class BlogView(generic.ListView):
    template_name = 'blogs/blog.html'
    model = Blog

class BlogDetailView(generic.DetailView):
    template_name = 'blogs/detail_blog.html'
    model = Blog

class BlogCreateView(generic.CreateView):
    template_name = 'blogs/create_blog.html'
    model = Blog
    form_class = BlogCreateForm

class BlogUpdateView(generic.UpdateView):
    template_name = 'blogs/update_blog.html'
    model = Blog
    form_class = BlogUpdateForm

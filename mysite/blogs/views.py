from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.


class BlogView(generic.ListView):
    template_name = 'blogs/blog.html'


from django.shortcuts import render
from django.views import generic

from .models import About
# Create your views here.


class AboutView(generic.ListView):
    template_name = 'about/about.html'
    model = About
    context_object_name = 'about'

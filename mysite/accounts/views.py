from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser

# Create your views here.


class ProfileView(generic.ListView):
    template_name = 'accounts/profile.html'
    model = CustomUser

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser

# Create your views here.


def user_profile_view(request):
    template = 'accounts/profile.html'

    profile = CustomUser.objects.all()

    context = {
        'profiles': profile
    }
    return render(request, template, context)

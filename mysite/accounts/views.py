from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser

from .forms import UserCreationForm
# Create your views here.


def user_profile_view(request):
    template = 'accounts/profile.html'

    profile = CustomUser.objects.all()

    context = {
        'profiles': profile
    }
    return render(request, template, context)

def sign_up_view(request):
    template = 'accounts/signup.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, template, context)

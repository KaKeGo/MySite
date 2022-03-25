from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from .models import Profile, CustomUser
from .forms import (
    UserCreationForm,
    UserUpdateForm,
    ProfileUpdateForm,
    PasswordUpdateForm
)
# Create your views here.


class PasswordUpdateView(PasswordChangeView):
    template_name = 'accounts/password_update.html'
    form_class = PasswordUpdateForm
    success_url = reverse_lazy('accounts:profile')

class ProfileView(generic.DetailView):
    template_name = 'accounts/profile.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['profile'] = profile
        return context

class ProfileUpdateView(generic.UpdateView):
    model = Profile
    template_name = 'accounts/profile_update.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('accounts:profile_update')

    def get_object(self):
        return self.request.user

# @login_required
# def user_profile_view(request):
#     template = 'accounts/profile1.html'
#
#     profile = CustomUser.objects.all()
#
#     context = {
#         'profiles': profile
#     }
#     return render(request, template, context)

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

def login_user_view(request):
    template = 'accounts/signin.html'

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('blogs:blog')
        else:
            return render('accounts:login')
    else:
        context = {}
        return render(request, template, context)

def logout_view(request):
    auth.logout(request)
    return redirect('blogs:blog')

# @login_required
# def update_profile_view(request):
#     templates = 'accounts/update_profile.html'
#
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts:profile')
#     else:
#         form = UserUpdateForm(instance=request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, templates, context)


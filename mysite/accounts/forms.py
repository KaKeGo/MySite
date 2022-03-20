from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm as CreateUser

from .models import CustomUser


class UserCreationForm(CreateUser):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'regimen')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.regimen = self.cleaned_data['regimen']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')

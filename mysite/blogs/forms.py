from django import forms

from .models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image')

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image')

class BlogDeleteForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

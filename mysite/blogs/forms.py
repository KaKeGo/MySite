from django import forms

from .models import Blog, Category


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image', 'category')

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image')

    def save(self, commit=True):
        blog = self.instance
        blog.title = self.cleaned_data['title']
        blog.body = self.cleaned_data['body']
        if self.cleaned_data['image']:
            blog.image = self.cleaned_data['image']

        if commit:
            blog.save()
        return blog

class BlogDeleteForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

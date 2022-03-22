from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from accounts.models import CustomUser
from .models import Blog
from .forms import BlogCreateForm, BlogUpdateForm

# Create your views here.


class BlogView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template = 'blogs/blog.html'

        blog = Blog.objects.all()

        context = {
            'blogs': blog
        }
        return render(request, template, context)

class BlogDetailView(generic.DetailView):
    template_name = 'blogs/detail_blog.html'
    model = Blog
    context_object_name = 'blogs'

class BlogCreateView(generic.View):
    def get(self, request, *args, **kwargs):
        template = 'blogs/create_blog.html'
        return render(request, template)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BlogCreateForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = self.request.user
                obj.save()
                return redirect('blogs:blog')
        else:
            form = BlogCreateForm()
        context = {
            'form': form,
        }
        return render(request, template, context)

class BlogUpdateView(generic.UpdateView):
    template_name = 'blogs/update_blog.html'
    model = Blog
    form_class = BlogUpdateForm

class BlogDeleteView(generic.DeleteView):
    template_name = 'blogs/delete_blog.html'
    model = Blog
    success_url = reverse_lazy('blogs:blog')

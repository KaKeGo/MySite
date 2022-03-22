from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from accounts.models import CustomUser
from .models import Blog
from .forms import BlogCreateForm, BlogUpdateForm, BlogDeleteForm

# Create your views here.


class BlogView(generic.ListView):
    template_name = 'blogs/blog.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 3


class BlogDetailView(generic.DetailView):
    template_name = 'blogs/detail_blog.html'
    model = Blog
    context_object_name = 'blogs'

    def post(self, request, slug, *args, **kwargs):
        blog = Blog.objects.get(slug=slug)
        blog.delete()
        return redirect(reverse_lazy('blogs:blog'))


class BlogCreateView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        template = 'blogs/create_blog.html'
        return render(request, template)

    def post(self, request, *args, **kwargs):
        template = 'blogs/create_blog.html'
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

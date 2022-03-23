from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from accounts.models import CustomUser
from .models import Blog, Category
from .forms import BlogCreateForm, BlogUpdateForm, BlogDeleteForm, CategoryCreateForm

# Create your views here.


class BlogView(generic.ListView):
    template_name = 'blogs/blog.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        return context

class BlogDetailView(generic.DetailView):
    template_name = 'blogs/detail_blog.html'
    model = Blog
    context_object_name = 'blogs'

    def post(self, request, slug, *args, **kwargs):
        blog = Blog.objects.get(slug=slug)
        blog.delete()
        return redirect(reverse_lazy('blogs:blog'))

def category_view(request, slug):
    template = 'blogs/category.html'

    blogs = Blog.objects.filter(category=slug)
    category = Category.objects.all()

    context = {
        'slug': slug,
        'blogs': blogs,
        'category': category,
    }
    return render(request, template, context)

class BlogCreateView(generic.CreateView):
    def get(self, request, *args, **kwargs):
        template = 'blogs/create_blog.html'
        category = Category.objects.all()
        context = {
            'categories': category,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        template = 'blogs/create_blog.html'
        if request.method == 'POST':
            form = BlogCreateForm(request.POST, request.FILES)
            form2 = CategoryCreateForm(request.POST)
            if form.is_valid() or form2.is_valid():
                if form2:
                    form2.save()
                elif form:
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
    def get(self, request, slug, *args, **kwargs):
        template = 'blogs/update_blog.html'
        blog = Blog.objects.get(slug=slug)
        form = BlogUpdateForm(
            initial={
                'title': blog.title,
                'body': blog.body,
                'image': blog.image,
            }
        )
        context = {
            'blog': blog,
            'form': form,
        }
        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        blog = get_object_or_404(Blog, slug=slug)
        if request.POST:
            form = BlogUpdateForm(request.POST or None, request.FILES or None, instance=blog)
            if form.is_valid():
                form.save()
                return redirect('blogs:detail', slug=slug)

# def update_blog_view(request, slug):
#     template = 'blogs/update_blog.html'
#
#     blog = get_object_or_404(Blog, slug=slug)
#     if request.POST:
#         form = BlogUpdateForm(request.POST or None, request.FILES or None, instance=blog)
#         if form.is_valid():
#             form.save()
#             return redirect('blogs:detail', slug=slug)
#     form = BlogUpdateForm(
#         initial={
#             'title': blog.title,
#             'body': blog.body,
#             'image': blog.image,
#         }
#     )
#     context = {
#         'form': form,
#         'blog': blog,
#     }
#     return render(request, template, context)

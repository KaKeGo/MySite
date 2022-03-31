from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser
from .models import Blog, Category
from .forms import BlogCreateForm, BlogUpdateForm, BlogDeleteForm, CategoryCreateForm

# Create your views here.

def like_view(request, pk):
    like = get_object_or_404(Blog, id=request.POST.get('likes'))
    if like.likes.filter(id=request.user.id).exists():
        like.likes.remove(request.user)
    else:
        like.likes.add(request.user)
    return redirect('blogs:blog')

class BlogView(generic.ListView):
    template_name = 'blogs/blog.html'
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['user'] = profile
        return context

    def get_context_data(self, *args, **kwargs):
        category = Category.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context['category'] = category
        return context


def blog_data_view(request, num_blogs, *args, **kwargs):
    visible = 3
    upper = num_blogs
    lower = upper - visible
    size = Blog.objects.all().count()

    blogs = Blog.objects.all()

    data = []
    for blog in blogs:
        item = {
            'id': blog.id,
            'title': blog.title,
            'body': blog.body,
            'image': blog.image.url,
            'category': blog.category,
            'likes': True if request.user in blog.likes.all() else False,
            'count': blog.total_likes,
            'author': blog.author.username,
            'slug': blog.slug,
            'create_on': blog.create_on,
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})

def like_unlike_post(request):
    pk = request.POST.get('pk')
    blog = Blog.objects.get(pk=pk)
    if request.user in blog.likes.all():
        likes = False
        blog.likes.remove(request.user)
    else:
        likes = True
        blog.likes.add(request.user)
    return JsonResponse({'likes': likes, 'count': blog.total_likes})

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
        form = BlogCreateForm()
        category = Category.objects.all()
        context = {
            'form': form,
            'categories': category,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BlogCreateForm(request.POST, request.FILES)
            form2 = CategoryCreateForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = self.request.user
                obj.save()
                return redirect('blogs:blog')
            elif form2.is_valid():
                form2.save()
                return redirect('blogs:create')

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

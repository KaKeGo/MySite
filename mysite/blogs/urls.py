from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    BlogView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    # update_blog_view,
    category_view,
    blog_data_view,
)


app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('data/', blog_data_view, name='blog_data'),
    path('create/', login_required(BlogCreateView.as_view()), name='create'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('detail/<slug:slug>/update/', login_required(BlogUpdateView.as_view()), name='update'),
    # path('detail/<slug:slug>/update/', update_blog_view, name='update'),
    path('category/<slug:slug>', category_view, name='category'),
]

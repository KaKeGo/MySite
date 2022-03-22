from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    BlogView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
)


app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('create/', login_required(BlogCreateView.as_view()), name='create'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('detail/<slug:slug>/update/', login_required(BlogUpdateView.as_view()), name='update'),
]

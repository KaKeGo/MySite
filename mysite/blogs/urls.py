from django.urls import path, include

from .views import (
    BlogView,
    BlogDetailView,
    BlogCreateView,
)


app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
]
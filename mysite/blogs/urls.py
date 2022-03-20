from django.urls import path, include

from .views import (
    BlogView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('detail/<slug:slug>/update/', BlogUpdateView.as_view(), name='update'),
    path('detail/<slug:slug>/delete/', BlogDeleteView.as_view(), name='delete'),
]

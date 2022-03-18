from django.urls import path, include

from .views import (
    BlogView,
    BlogDetailView,
)


app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
]
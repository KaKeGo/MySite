from django.urls import path, include

from .views import (
    BlogView,
)


app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
]
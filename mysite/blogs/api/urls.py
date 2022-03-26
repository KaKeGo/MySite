from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoryApiView,
    CategoryUpDelView,
    BlogApiView,
    BlogApiDelUpdView,
)

app_name = 'blogs-api'

urlpatterns = [
    # path('category/', category_list, name='api-category'),
    path('category/', CategoryApiView.as_view(), name='api-category-list-post'),
    path('blogs/', BlogApiView.as_view(), name='api-blog-list-post'),
    path('category/<int:id>/', CategoryUpDelView.as_view(), name='api-category-update-delete'),
    path('blogs/<int:id>/', BlogApiDelUpdView.as_view(), name='api-blog-update-delete'),
]

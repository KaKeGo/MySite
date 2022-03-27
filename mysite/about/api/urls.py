from django.urls import path, include

from .views import (
    AboutLisPosApiView,
    AboutDelUpdApiView,
)

app_name = 'about-api'

urlpatterns = [
    path('', AboutLisPosApiView.as_view(), name='api-about-list-post'),
    # path('blogs/', BlogApiView.as_view(), name='api-blog-list-post'),
    path('del-upd/<int:id>/', AboutDelUpdApiView.as_view(), name='api-about-update-delete'),
    # path('blogs/<int:id>/', BlogApiDelUpdView.as_view(), name='api-blog-update-delete'),
]

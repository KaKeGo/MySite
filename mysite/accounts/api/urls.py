from django.urls import path

from .views import (
    ProfileLisPosApiView,
    ProfileUpdDelApiView,
    CustomUserLisPosApiView,
    CustomUserUpdDelApiView,
)

app_name = 'accounts-api'

urlpatterns = [
    path('', ProfileLisPosApiView.as_view(), name='api-accounts-list-post'),
    path('users/', CustomUserLisPosApiView.as_view(), name='api-users-list-post'),
    path('del-upd/<int:id>/', ProfileUpdDelApiView.as_view(), name='api-accounts-update-delete'),
    path('users/<int:id>/', CustomUserUpdDelApiView.as_view(), name='api-blog-users-delete'),
]

from django.urls import path, include

from .views import (
    user_profile_view,
)


app_name = 'accounts'

urlpatterns = [
    path('profile/', user_profile_view, name='profile'),
]

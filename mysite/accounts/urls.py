from django.urls import path, include

from .views import (
    user_profile_view,
    sign_up_view,
)


app_name = 'accounts'

urlpatterns = [
    path('profile/', user_profile_view, name='profile'),
    path('sign-up/', sign_up_view, name='sign_up'),
]

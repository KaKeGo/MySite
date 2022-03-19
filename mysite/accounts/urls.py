from django.urls import path, include

from .views import (
    user_profile_view,
    sign_up_view,
    login_user_view,
    logout_view,
)


app_name = 'accounts'

urlpatterns = [
    path('profile/', user_profile_view, name='profile'),
    path('sign-up/', sign_up_view, name='sign_up'),
    path('sign-in/', login_user_view, name='sign_in'),
    path('logout/', logout_view, name='logout'),
]

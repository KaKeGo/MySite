from django.urls import path, include
from django.contrib.auth.decorators import login_required


from .views import (
    # user_profile_view,
    sign_up_view,
    login_user_view,
    logout_view,
    # update_profile_view,
    ProfileView,
    ProfileUpdateView,
    PasswordUpdateView,
)


app_name = 'accounts'

urlpatterns = [
    path('sign-up/', sign_up_view, name='sign_up'),
    path('sign-in/', login_user_view, name='sign_in'),
    path('logout/', logout_view, name='logout'),
    # path('profile1/', user_profile_view, name='profile1'),
    path('<slug:slug>/profile/', login_required(ProfileView.as_view()), name='profile'),
    # path('profile/update/', update_profile_view, name='update'),
    path('<int:pk>/profile/update/', login_required(ProfileUpdateView.as_view()), name='profile_update'),
    path('password/', login_required(PasswordUpdateView.as_view()), name='password_update'),
]

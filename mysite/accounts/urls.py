from django.urls import path, include
from django.contrib.auth.decorators import login_required


from .views import (
    # user_profile_view,
    sign_up_view,
    login_user_view,
    logout_view,
    update_profile_view,
    ProfileView,
)


app_name = 'accounts'

urlpatterns = [
    # path('profile1/', user_profile_view, name='profile1'),
    path('<int:pk>/profile/', login_required(ProfileView.as_view()), name='profile'),
    path('profile/update/', update_profile_view, name='update'),
    path('sign-up/', sign_up_view, name='sign_up'),
    path('sign-in/', login_user_view, name='sign_in'),
    path('logout/', logout_view, name='logout'),
]

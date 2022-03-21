from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    AboutView,
    SkillCreateView,
)


app_name = 'about'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('add-skill/', login_required(SkillCreateView.as_view()), name='add_skill'),
]

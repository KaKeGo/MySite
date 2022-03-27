from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    AboutView,
)


app_name = 'about'

urlpatterns = [
    path('', login_required(AboutView.as_view()), name='about'),

]

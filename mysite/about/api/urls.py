from django.urls import path, include

from .views import (
    AboutLisPosApiView,
    AboutDelUpdApiView,
    SkillLisPosApiView,
    SkillUpdDelApiView,
)

app_name = 'about-api'

urlpatterns = [
    path('', AboutLisPosApiView.as_view(), name='api-about-list-post'),
    path('skills/', SkillLisPosApiView.as_view(), name='api-skills-list-post'),
    path('del-upd/<int:id>/', AboutDelUpdApiView.as_view(), name='api-about-update-delete'),
    path('skills/<int:id>/', SkillUpdDelApiView.as_view(), name='api-blog-skills-delete'),
]

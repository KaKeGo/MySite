from django.urls import path

from .views import (
    ContactPoLiApiView,
    ContactDelUpdApiView,
    ContactMessageLisPosApiView,
    ContactMessageDelUpdApiView,
)

app_name = 'contacts-api'

urlpatterns = [
    path('', ContactPoLiApiView.as_view(), name='api-contact-post-list'),
    path('message/', ContactMessageLisPosApiView.as_view(), name='api-message-post-list'),
    path('del-upd/<int:id>/', ContactDelUpdApiView.as_view(), name='api-category-update-delete'),
    path('message/del-upd/<int:id>/', ContactMessageDelUpdApiView.as_view(), name='api-message-update-delete'),
]
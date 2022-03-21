from django.urls import path, include

from .views import (
    ContactsView,
    ContactMessageCreate,
    ContactMessgesList,
    ContactMessageDetail,
)


app_name = 'contacts'

urlpatterns = [
    path('', ContactsView.as_view(), name='contact'),
    path('message/', ContactMessageCreate.as_view(), name='message'),
    path('message/list/', ContactMessgesList.as_view(), name='list'),
    path('message/<slug:slug>/', ContactMessageDetail.as_view(), name='detail'),
]

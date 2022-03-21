from django.urls import path, include

from .views import (
    ContactsView,
    ContactMessageCreate,
    ContactMessgesList,
)


app_name = 'contacts'

urlpatterns = [
    path('', ContactsView.as_view(), name='contact'),
    path('message/', ContactMessageCreate.as_view(), name='message'),
    path('message/list/', ContactMessgesList.as_view(), name='list'),
]

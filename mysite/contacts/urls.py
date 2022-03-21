from django.urls import path, include

from .views import (
    ContactsView,
    ContactMessageCreateView,
    ContactMessgesListView,
    ContactMessageDetailView,
    ContactMessageDeleteView,
)


app_name = 'contacts'

urlpatterns = [
    path('', ContactsView.as_view(), name='contact'),
    path('message/', ContactMessageCreateView.as_view(), name='message'),
    path('message/list/', ContactMessgesListView.as_view(), name='list'),
    path('message/<slug:slug>/', ContactMessageDetailView.as_view(), name='detail'),
    path('message/<slug:slug>/delete/', ContactMessageDeleteView.as_view(), name='delete'),
]

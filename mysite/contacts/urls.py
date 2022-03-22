from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    ContactsView,
    ContactMessgesListView,
    ContactMessageDetailView,
    ContactMessageDeleteView,
)


app_name = 'contacts'

urlpatterns = [
    path('', ContactsView.as_view(), name='contact'),
    path('message/list/', login_required(ContactMessgesListView.as_view()), name='list'),
    path('message/<slug:slug>/', login_required(ContactMessageDetailView.as_view()), name='detail'),
    path('message/<slug:slug>/delete/', login_required(ContactMessageDeleteView.as_view()), name='delete'),
]

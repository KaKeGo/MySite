from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import (
    ContactsView,
    ContactMessgesListView,
    ContactMessageDetailView,

)


app_name = 'contacts'

urlpatterns = [
    path('', login_required(ContactsView.as_view()), name='contact'),
    path('message/list/', login_required(ContactMessgesListView.as_view()), name='list'),
    path('message/<slug:slug>/', login_required(ContactMessageDetailView.as_view()), name='detail'),
]

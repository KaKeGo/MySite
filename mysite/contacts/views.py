from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.


class ContactsView(generic.ListView):
    template_name = 'contacts/contact.html'
    model = None

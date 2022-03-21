from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Contact, ContactMessage
from .forms import ContactMessageForm
# Create your views here.


class ContactsView(generic.ListView):
    template_name = 'contacts/contact.html'
    model = Contact
    context_object_name = 'contacts'

class ContactMessgesListView(generic.ListView):
    template_name = 'contacts/message_list.html'
    model = ContactMessage
    context_object_name = 'messages'

class ContactMessageCreateView(generic.CreateView):
    template_name = 'contacts/contact_message.html'
    model = Contact
    form_class = ContactMessageForm
    context_object_name = 'messages'
    success_url = reverse_lazy('contacts:contact')

class ContactMessageDetailView(generic.DetailView):
    template_name = 'contacts/message_detail.html'
    model = ContactMessage
    context_object_name = 'messages'

class ContactMessageDeleteView(generic.DeleteView):
    template_name = 'contacts/message_delete.html'
    model = ContactMessage
    success_url = reverse_lazy('contacts:list')

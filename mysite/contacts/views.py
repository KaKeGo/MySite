from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import Contact, ContactMessage
from .forms import ContactMessageForm
# Create your views here.


class ContactsView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template = 'contacts/contact.html'
        contact = Contact.objects.all()
        context = {
            'contacts': contact,
        }
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.postman = self.request.user
            obj.save()
            return redirect(reverse_lazy('contacts:contact'))

class ContactMessgesListView(generic.ListView):
    def get_queryset(self):
        qs = ContactMessage.objects.all()
        if self.kwargs.get('slug'):
            qs = qs.filter(tags__name=self.kwargs['slug'])
        return qs

    def get(self, request, *args, **kwargs):
        templates = 'contacts/message_list.html'
        message = ContactMessage.objects.all()
        context = {
            'messages': message
        }
        return render(request, templates, context)

class ContactMessageDetailView(generic.DetailView):
    template_name = 'contacts/message_detail.html'
    model = ContactMessage
    context_object_name = 'messages'

    def post(self, request, slug, *args, **kwargs):
        message = ContactMessage.objects.get(slug=slug)
        message.delete()
        return redirect(reverse_lazy('contacts:list'))

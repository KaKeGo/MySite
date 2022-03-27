from rest_framework import status, views, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from contacts.models import Contact, ContactMessage
from .serializers import ContactSerializer, ContactMessageSerializer


class ContactMessageDelUpdApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

class ContactMessageLisPosApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ContactMessageSerializer
    queryset = ContactMessage.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class ContactDelUpdApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                           mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

class ContactPoLiApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

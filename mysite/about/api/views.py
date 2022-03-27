from rest_framework import status, views, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from about.models import About, Skills
from .serializers import AboutSerializer, SkillsSerializer


class AboutDelUpdApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
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

class AboutLisPosApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

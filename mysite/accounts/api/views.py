from rest_framework import status, views, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUser, Profile
from .serializers import ProfileSerializer, CustomUserSerializer


class CustomUserUpdDelApiView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.ListModelMixin,
                              mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
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


class CustomUserLisPosApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class ProfileUpdDelApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = ('id')

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

class ProfileLisPosApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

from rest_framework import status, views, generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from blogs.models import Category, Blog
from .serializers import CategorySerializer, BlobSerializer


class BlogApiDelUpdView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = BlobSerializer
    queryset = Blog.objects.all()
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

class BlogApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BlobSerializer
    queryset = Blog.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CategoryUpDelView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
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

class CategoryApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

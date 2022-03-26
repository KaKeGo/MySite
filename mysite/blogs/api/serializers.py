from rest_framework import serializers

from blogs.models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class BlobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image', 'category', 'likes', 'author', 'slug')

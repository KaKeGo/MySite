from rest_framework import serializers

from contacts.models import Contact, ContactMessage


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'title', 'body')

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ('id', 'name', 'body', 'postman', 'slug')

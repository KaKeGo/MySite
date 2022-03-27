from rest_framework import serializers

from about.models import About, Skills


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'name', 'description', 'avatar', 'skills')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('id', 'title', 'score')

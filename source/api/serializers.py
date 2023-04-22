from rest_framework import serializers
from gallery.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'sign', 'users', 'created_at', 'updated_at']

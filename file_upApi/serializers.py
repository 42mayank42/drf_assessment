from dataclasses import field
from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class MultipleFileSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField()
    )



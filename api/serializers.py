from rest_framework import serializers

from memes.models import Mem


class MemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mem
        fields = ['title', 'body', 'image']

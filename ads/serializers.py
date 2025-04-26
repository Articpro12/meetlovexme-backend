from rest_framework import serializers
from .models import Ad, AdImage

class AdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = ['image']

class AdSerializer(serializers.ModelSerializer):
    images = AdImageSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'name', 'city', 'height', 'colour', 'phone', 'whatsapp', 'telegram', 'images']

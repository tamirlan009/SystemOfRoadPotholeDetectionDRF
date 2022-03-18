from rest_framework import serializers
from .models import DetectedTable, Images


class ImagesSerializer(serializers.ModelSerializer):
    """
    Image table serializer
    """

    class Meta:
        model = Images
        fields = '__all__'


class DetectedTableSerializer(serializers.ModelSerializer):
    """
    DetectedTable table serializer
    """

    class Meta:
        model = DetectedTable
        fields = '__all__'


class DetailDetectedTableSerializer(serializers.ModelSerializer):
    """
    DetectedTable table serializer with images
    """

    images = ImagesSerializer(many=True)

    class Meta:
        model = DetectedTable
        fields = '__all__'

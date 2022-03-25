from rest_framework import serializers
from .models import DetectionTable, Images


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
        model = DetectionTable
        fields = '__all__'


class DetailDetectedTableSerializer(serializers.ModelSerializer):
    """
    DetectedTable table serializer with images
    """

    images = ImagesSerializer(many=True)

    class Meta:
        model = DetectionTable
        fields = '__all__'

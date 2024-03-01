from rest_framework import serializers
from .models import VideoFile, Toifalash, Test, PDFFile

class ToifalashFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toifalash
        fields = '__all__'

class VideoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFile
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    toifalash = ToifalashFileSerializer()

    class Meta:
        model = Test
        fields = '__all__'

class PdfFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFFile
        fields = '__all__'

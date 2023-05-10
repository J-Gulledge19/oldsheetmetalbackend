from .models import Job, Download
from rest_framework import serializers

        
class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'
        
class JobSerializer(serializers.ModelSerializer):
    downloadenance = DownloadSerializer(many = True, read_only=True)
    class Meta:
        model = Job
        fields = '__all__'
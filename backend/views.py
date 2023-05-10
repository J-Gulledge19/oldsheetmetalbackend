from django.shortcuts import render
from .models import Job, Download
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import JobSerializer, DownloadSerializer

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    
class DownloadViewSet(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    permission_classes = [permissions.AllowAny]
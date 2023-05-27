from django.shortcuts import render
from .models import Job, Download, Weight
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import JobSerializer, DownloadSerializer, WeightSerializer

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    
class DownloadViewSet(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer
    permission_classes = [permissions.AllowAny]
    
# class WeightViewSet(viewsets.ModelViewSet):
#     queryset = Weight.objects.all()
#     serializer_class = WeightSerializer
#     permission_classes = [permissions.AllowAny]
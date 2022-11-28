from .serializers import DocumentSerializer
from .models import Document
from rest_framework import generics
from django.shortcuts import render

class DocumentUploadView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class= DocumentSerializer

def home(request):
    return render(request, 'home.html')
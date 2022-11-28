from rest_framework import generics
from .serializers import ReaderSerializer
from .models import Reader

class ReaderViews(generics.ListCreateAPIView):
    queryset= Reader.objects.all()
    serializer_class= ReaderSerializer
from rest_framework import generics
from .models import Ad
from .serializers import AdSerializer

class AdListAPIView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

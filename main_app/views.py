from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Plant
from .serializers import PlantSerializer

# Create your views here.
# 🌿 View All Plants + Add New Plant
class PlantIndex(APIView):
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
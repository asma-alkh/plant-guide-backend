from rest_framework import serializers 
from .models import Plant, Soil, Schedule, Favorite

#  Soil Serializer
class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil
        fields = '__all__'
#  Plant Serializer
class PlantSerializer(serializers.ModelSerializer):
    soil = SoilSerializer(read_only=True)
    class Meta:
        model = Plant 
        fields = '__all__' 

# Schedule Serializer

class ScheduleSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)

    class Meta:
        model = Schedule 
        fields = '__al__'

# Favorite Serializer
class FavoriteSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)

    class Meta:
        model = Favorite
        fielda = '__all__'
        
from rest_framework import serializers 
from .models import Plant, Soil, Favorite, Category

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

# Favorite Serializer
class FavoriteSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)

    class Meta:
        model = Favorite
        fielda = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        modelde : Category 
        fields = '__all__'
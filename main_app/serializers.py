from rest_framework import serializers
from .models import Plant, Soil, Favorite, Category, Schedule, UserPlant
from django.contrib.auth.models import User
from .models import Profile

#  Soil Serializer
class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soil
        fields = "__all__"

# Plant Serializer
class PlantSerializer(serializers.ModelSerializer):
    soil = SoilSerializer(read_only=True)
    category = serializers.StringRelatedField(read_only=True) 

    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "image_url",
            "description",
            "watering_frequency",
            "sunlight",
            "soil",
            "category",
        ]

# Schedule Serializer
class ScheduleSerializer(serializers.ModelSerializer):
    plant_name = serializers.CharField(source='plant.name', read_only=True)

class ScheduleSerializer(serializers.ModelSerializer):
    plant_name = serializers.CharField(source='plant.name', read_only=True)

    class Meta:
        model = Schedule
        fields = ["id", "plant", "plant_name", "task_name", "note", "date", "day", "is_done", "user"]
        read_only_fields = ["user"]

#  Favorite Serializer
class FavoriteSerializer(serializers.ModelSerializer):
    plant = PlantSerializer(read_only=True)
    plant_id = serializers.PrimaryKeyRelatedField(
        queryset=Plant.objects.all(),
        source="plant",
        write_only=True
    )

    class Meta:
        model = Favorite
        fields = ["id", "plant", "plant_id", "added_at"]
        read_only_fields = ["added_at"]

#  Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  
        fields = "__all__"

class UserPlantSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) 
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = UserPlant
        fields = ['id', 'user', 'name', 'description', 'advice', 'image', 'category', 'category_id', 'created_at']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "bio", "location", "profile_image"]
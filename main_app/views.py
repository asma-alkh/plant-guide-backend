from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .models import Plant, Soil, Favorite, Category
from .serializers import PlantSerializer, SoilSerializer,FavoriteSerializer,CategorySerializer 


# Create your views here.
User = get_user_model()

class Home(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        content = {
            "message": "🌿 Welcome to the Plant Guide API!",
            "info": "Here you can learn how to care for your plants."
        }
        return Response(content)
    def post(self, request):
        data = request.data
        content = {
            "message": "🌱 Thank you for connecting with Plant Guide!",
            "your_data": data
        }
        return Response(content)
#  View All Plants + Add New Plant CR 
class PlantsIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            serializer = PlantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Add RUD
class PlantDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, plant_id):
        try:
            plant = get_object_or_404(Plant, id=plant_id)
            serializer = PlantSerializer(plant)
            return Response(serializer.data)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, plant_id):
        try:
            plant = get_object_or_404(Plant, id=plant_id)
            serializer = PlantSerializer(plant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, plant_id):
        try:
            plant = get_object_or_404(Plant, id=plant_id)
            plant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SoilIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        soils = Soil.objects.all()
        serializer = SoilSerializer(soils, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SoilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SoilDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, soil_id):
        soil = get_object_or_404(Soil, id=soil_id)
        serializer = SoilSerializer(soil)
        return Response(serializer.data)
    

    def put(self, request, soil_id):
        soil = get_object_or_404(Soil, id=soil_id)
        serializer = SoilSerializer(soil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, soil_id):
        soil = get_object_or_404(Soil, id=soil_id)
        soil.delete()    
        return Response(status=status.HTTP_204_NO_CONTENT)

# Favorite
class FavoriteIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorite = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorite, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FavoriteDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, favorite_id):
        favorite = get_object_or_404(Favorite, id=favorite_id)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)
    def delete(self, request, favorite_id):
        favorite = get_object_or_404(Favorite, id=favorite_id)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryIndex(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# Register (Sign Up)
class RegisterView(APIView):
    """
    This endpoint allows new users to create an account.
    Accessible by anyone (no authentication required).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        # Check required fields
        if not username or not email or not password:
            return Response(
                {"error": "Please provide username, email, and password."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "This username is already taken."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password 
        )
        return Response(
            {
                "message": "Account created successfully 🌿",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            },
            status=status.HTTP_201_CREATED
        )
# Login (Sign In)

class LogInView(APIView):
    """
    Authenticate existing users and return a JWT token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message": f"Welcome back, {username}! 🌱",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

# Logout 
class LogoutView(APIView):
    """
    Logout user by blacklisting their refresh token.
    (User must be authenticated)
    """  
    permission_classes = [AllowAny]


    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "You have been logged out successfully "},
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            return Response(
                {"error": "Invalid or missing refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )

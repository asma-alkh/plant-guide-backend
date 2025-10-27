from django.urls import path

from .views import PlantsIndex,PlantDetail

urlpatterns = [
    path('plants/', PlantsIndex.as_view(), name='plants_index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant_detail'),
]
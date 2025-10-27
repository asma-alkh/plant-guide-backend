from django.urls import path

from .views import PlantsIndex,PlantDetail, SoilIndex, SoilDetail

urlpatterns = [
    path('plants/', PlantsIndex.as_view(), name='plants_index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant_detail'),
    path('soils/', SoilIndex.as_view(), name='soil_index'), 
    path('soils/<int:soil_id>/', SoilDetail.as_view(), name='soil_detail')
]
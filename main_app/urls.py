from django.urls import path

from .views import PlantsIndex,PlantDetail, SoilIndex, SoilDetail, ScheduleIndex, ScheduleDetail, FavoriteIndex, FavoriteDetail, CategoryIndex, Home, RegisterView, LogInView, LogoutView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('plants/', PlantsIndex.as_view(), name='plants_index'),
    path('plants/<int:plant_id>/', PlantDetail.as_view(), name='plant_detail'),
    path('soils/', SoilIndex.as_view(), name='soil_index'), 
    path('soils/<int:soil_id>/', SoilDetail.as_view(), name='soil_detail'),
    path('schedules/', ScheduleIndex.as_view(), name='schedules_index'),
    path('schedules/<int:schedule_id>/', ScheduleDetail.as_view(), name='schedules_detail'),
    path('favorites/', FavoriteIndex.as_view(), name='favorites_index'),
    path('favorites/<int:favorite_id>/', FavoriteDetail.as_view(), name='favorites_detail'),
    path('categories/', CategoryIndex.as_view(), name='category_index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LogInView.as_view(), name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
]
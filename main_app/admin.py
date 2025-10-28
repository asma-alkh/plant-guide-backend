from django.contrib import admin
from .models import Plant, Soil, Schedule, Favorite, Category 
# Register your models here.
admin.site.register(Plant)
admin.site.register(Soil)
admin.site.register(Schedule)
admin.site.register(Favorite)
admin.site.register(Category)
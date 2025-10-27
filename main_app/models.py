from django.db import models
from django.utils.text import slugify
# Create your models here.
# first Model Plant 

class Soil(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    fertilizing_instructions = models.TextField(blank=True, null=True)
    mixture_of = models.CharField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return self.name
    

class Plant(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    watering_frequency = models.CharField(max_length=100)
    sunlight = models.CharField(max_length=100, blank=True, null=True)
    soil = models.ForeignKey(Soil, on_delete=models.SET_NULL, null=True, related_name='plants')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.name

class Schedule(models.Model):
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='schedules')
    task_name = models.CharField(max_length=100) #Like Watering the plant or pruning the leaves
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task_name} - {self.plant.name}"
    

class Favorite(models.Model):
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, related_name='favorites')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorits: {self.plant.name}"
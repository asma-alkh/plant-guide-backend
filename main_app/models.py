from django.db import models
from django.utils.text import slugify
# Create your models here.
# first Model Plant 

class Plant(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    watering_frequency = models.CharField(max_length=100)
    sunlight = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.name
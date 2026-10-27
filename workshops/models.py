from django.db import models
from django.urls import reverse
from recipes.models import Recipe

class Instructor(models.Model):
    name = models.CharField(max_length=150, verbose_name="Instructor Name")
    bio = models.TextField(verbose_name="Biography")
    specialty = models.CharField(max_length=100, verbose_name="Specialty Cuisine")

    def __str__(self):
        return self.name

class Workshop(models.Model):
    title = models.CharField(max_length=200, verbose_name="Workshop Title")
    date = models.DateTimeField(verbose_name="Workshop Date & Time")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='workshops', verbose_name="Lead Instructor")
    recipes = models.ManyToManyField(Recipe, related_name='workshops', verbose_name="Featured Recipes")

    def get_absolute_url(self):
        return reverse('workshop_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
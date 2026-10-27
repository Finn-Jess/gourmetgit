from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Recipe Title")
    ingredients = models.TextField(verbose_name="Ingredients List")
    instructions = models.TextField(verbose_name="Cooking Instructions")
    prep_time = models.PositiveIntegerField(verbose_name="Preparation Time (minutes)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes', verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
from django.shortcuts import render
from recipes.models import Recipe
from workshops.models import Workshop

def home_view(request):
    recipes = Recipe.objects.all().order_by('-created_at')[:3]
    workshops = Workshop.objects.all().order_by('date')[:3]
    context = {
        'recipes': recipes,
        'workshops': workshops,
    }
    return render(request, 'core/home.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
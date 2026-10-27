from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list_view, name='recipe_list'),
    path('create/', views.recipe_create_view, name='recipe_create'),
    path('<int:pk>/', views.recipe_detail_view, name='recipe_detail'),
    path('<int:pk>/edit/', views.recipe_update_view, name='recipe_update'),
    path('<int:pk>/delete/', views.recipe_delete_view, name='recipe_delete'),
]
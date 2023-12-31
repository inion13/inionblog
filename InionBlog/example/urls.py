from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path('recipes/edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipes/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]

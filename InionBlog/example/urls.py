from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<int:recipe_id>', views.recipe, name='recipe'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.user_registration, name='registration')
    # path('create/', views.create_item, name='create'),
    # path('read/<int:item_id', views.read_item, name='read'),
    # path('update/<int:item_id', views.update_item, name='update'),
    # path('delete/<int:item_id', views.delete_item, name='delete')
]

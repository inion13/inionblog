from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .utils import CustomLoginView

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('recipes/create/', views.create_recipe, name='create_recipe'),
    path('recipes/edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipes/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

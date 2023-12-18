from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, related_name='deleted_comments', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.user.username} - {self.recipe.title} - {self.created_at}'

from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    steps = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)

    def __str__(self):
        return self.title

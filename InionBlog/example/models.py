from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.title

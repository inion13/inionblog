from django.db import models


class Recipe(models.Model):
    objects = None
    title = models.CharField(max_length=9000)
    description = models.CharField(max_length=9000)

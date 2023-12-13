from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=9000)
    description = models.CharField(max_length=9000)

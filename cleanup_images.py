import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InionBlog.settings')
django.setup()

from example.models import Recipe

IMAGE_DIR = '/media'

image_files = os.listdir(IMAGE_DIR)

used_images = Recipe.objects.values_list('image', flat=True)

for image_file in image_files:
    if image_file not in used_images:
        os.remove(os.path.join(IMAGE_DIR, image_file))

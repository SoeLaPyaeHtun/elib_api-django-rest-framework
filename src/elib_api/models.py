from django.db import models

# Create your models here.

class Author(models.Model):
    pen_name = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True)
    photo = models.ImageField(
        upload_to="src/photo", blank=True, null=True
    )
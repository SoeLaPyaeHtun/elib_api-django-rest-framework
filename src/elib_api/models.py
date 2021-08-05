from django.db import models

# Create your models here.


class Author(models.Model):
    pen_name = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    date_of_birth = models.DateField(blank=True)
    photo = models.ImageField(
        upload_to="author_img/", default="author_img/defaul.jpg"
    )

    def __str__(self):
        return self.pen_name

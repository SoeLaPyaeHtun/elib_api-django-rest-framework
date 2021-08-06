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


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(Author,blank=True, null=True, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,blank=True, null=True)
    cover_img = models.ImageField(
        upload_to="book_cover_img/", default="book_cover_img/default.jpg"
    )
    file = models.FileField(
        upload_to="book_file/",blank=True, null=True
    )

    def __str__(self):
        return self.title    
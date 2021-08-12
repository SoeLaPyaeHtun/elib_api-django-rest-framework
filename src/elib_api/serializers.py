from django.db import models
from rest_framework import serializers
from .models import Book,Author, Category

class PostBookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

class PostAuthorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class PostCategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
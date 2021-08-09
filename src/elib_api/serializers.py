from django.db import models
from rest_framework import serializers
from .models import Book

class PostModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
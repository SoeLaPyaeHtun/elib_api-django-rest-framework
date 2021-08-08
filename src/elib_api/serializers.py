from django.db import models
from rest_framework import serializers
from .models import Book

class GetModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Book
        field = "__all__"
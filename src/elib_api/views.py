from django.http import response
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from .serializers import PostBookModelSerializer,PostAuthorModelSerializer,PostCategoryModelSerializer
from .models import Author, Book, Category


class PostBookModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = PostBookModelSerializer
    queryset = Book.objects.all()


class PostAuthorModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = PostAuthorModelSerializer
    queryset = Author.objects.all()


class PostCategoryModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategoryModelSerializer
    queryset = Category.objects.all()


# class PostListAPIViewSet(viewsets.ViewSet):
#     def list(self, request):
#         return Response({"method" : "list"}, status=200)

#     def create(self, request):
#         return Response({"method" : "create"}, status=200)

#     def retrieve(self, request, pk=None):
#         return Response({"method" : "retrieve"}, status=200)

#     def update(self, request, pk=None):
#         return Response({"method" : "update"}, status=200)

#     def partial_update(self, request, pk=None):
#         return Response({"method" : "partial_update"}, status=200)

#     def destory(self, request, pk=None):
#         return Response({"method" : "destory"}, status=200)
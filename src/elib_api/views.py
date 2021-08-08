from django.http import response
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from .serializers import GetModelSerializer
from .models import Book


class GetModelAPIViewSet(viewsets.ModelViewSet):
    serializer_class = GetModelSerializer
    queryset = Book.objects.all

# class GetListAPIViewSet(viewsets.ViewSet):
#     def list(self, request,*args, **kwargs):
#         return Response({"method" : "list"}, status=200)
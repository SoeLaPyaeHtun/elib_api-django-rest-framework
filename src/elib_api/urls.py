from django.urls import path,include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import GetModelSerializer

router = DefaultRouter()
router.register('get-viewset', GetModelSerializer,basename='get-viewset')

urlpatterns = [
    path('viewsets/', include(router.urls))
]
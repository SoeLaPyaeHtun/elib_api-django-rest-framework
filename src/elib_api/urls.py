from django.urls import path,include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import PostModelAPIViewSet

router = DefaultRouter()
router.register('get-model-viewsets', PostModelAPIViewSet, basename='post-model-viewsets')

urlpatterns = [
    # path('viewsets/', include(router.urls)),
    path('viewsets/', include(router.urls)),
]
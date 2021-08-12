from django.urls import path,include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import PostBookModelAPIViewSet,PostAuthorModelAPIViewSet,PostCategoryModelAPIViewSet

router = DefaultRouter()
router.register('get-book-model-viewsets', PostBookModelAPIViewSet, basename='post-book-model-viewsets')
router.register('get-author-model-viewsets', PostAuthorModelAPIViewSet, basename='post-author-model-viewsets')
router.register('get-category-model-viewsets', PostCategoryModelAPIViewSet, basename='post-category-model-viewsets')

urlpatterns = [
    # path('viewsets/', include(router.urls)),
    path('viewsets/', include(router.urls)),
]
"""
Blog url
"""

from django.urls import path,include
from .views import PostViewSet,CommentViewSet,TagViewSet,CategoryViewSet
from rest_framework import routers


router=routers.SimpleRouter()
router.register('post',PostViewSet)
router.register('comment',CommentViewSet)
router.register('tag',TagViewSet)
router.register('category',CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from django.shortcuts import render , HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Post , Category , Comment , Tag
from .serializers import Post_serializer, Category_serializer , Comment_serializer , Tag_serializer


# viewsets give you all httpverbs in each models


class PostViewSet(ModelViewSet):
  queryset=Post.objects.all()
  serializer_class=Post_serializer
  

class CategoryViewSet(ModelViewSet):
  queryset=Category.objects.all()
  serializer_class=Category_serializer

class CommentViewSet(ModelViewSet):
  queryset=Comment.objects.all()
  serializer_class=Comment_serializer


class TagViewSet(ModelViewSet):
  queryset=Tag.objects.all()
  serializer_class=Tag_serializer
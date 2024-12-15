from rest_framework import serializers
from .models import Post,Category,Comment,Tag



class Post_serializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields='__all__'


class Category_serializer(serializers.ModelSerializer):
    class Meta:
      model=Category
      fields='__all__'


class Comment_serializer(serializers.ModelSerializer):
    class Meta:
      model=Comment
      fields='__all__'


class Tag_serializer(serializers.ModelSerializer):
     class Meta:
      model=Tag
      fields='__all__'
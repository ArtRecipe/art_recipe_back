from django.db.models import fields
from rest_framework import serializers
from .models import Post, PostImage, Material
from accounts.serializers import UserSerializer

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields="__all__"

class PostSerializer(serializers.ModelSerializer):
    writer=UserSerializer()
    material=MaterialSerializer()

    class Meta:
        model = Post
        fields=["writer", "title", "created_at", "updated_at", "thumbnail", "material", "color", "desc"]
        read_only_fields=["id", "created_at", "updated_at"]

class PostCreateSerializer(serializers.ModelSerializer):
    writer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ["writer", "title", "created_at", "updated_at", "thumbnail", "material", "color", "desc"]
        read_only_fields = ["id", "created_at", "updated_at"]


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"
from django.db.models import fields
from rest_framework import serializers
from .models import Post, PostImage, Material
from accounts.serializers import UserSerializer

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["name", "url"]

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage   
        fields = ["image"]

class PostSerializer(serializers.ModelSerializer):
    writer=UserSerializer()
    images=PostImageSerializer(many = True, read_only = True)
    materials=MaterialSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields=["id", "writer", "title", "created_at", "updated_at", "color", "desc", "url", "bookmarks", "images", "materials"]
        read_only_fields=["id", "writer", "created_at", "updated_at"]

class PostCreateSerializer(serializers.ModelSerializer):
    writer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    materials = MaterialSerializer(many = True)

    def create(self, validated_data):
        materials_data = validated_data.pop('materials')
        images_data = self.context["request"].FILES

        post = Post.objects.create(**validated_data)

        for image_data in images_data.getlist('image'):
            PostImage.objects.create(post = post, **image_data)
        
        for material_data in materials_data:
            Material.objects.create(post = post, **material_data)

        return post

    class Meta:
        model = Post
        fields =["id", "writer", "title", "created_at", "updated_at", "color", "desc", "url", "materials"]
        read_only_fields = ["id", "writer", "created_at", "updated_at"]
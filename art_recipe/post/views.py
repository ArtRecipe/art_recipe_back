from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import Post, Material, PostImage
from .serializers import (
    MaterialSerializer,
    PostSerializer,
    PostImageSerializer,
)

class MaterialViewSet(ModelViewSet):
    queryset=Material.objects.all()
    serializer_class=MaterialSerializer

class PostViewSet(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostImageView(CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


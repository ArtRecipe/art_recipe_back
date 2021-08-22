from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .models import Post, Material, PostImage
from .serializers import (
    MaterialSerializer,
    PostSerializer,
    PostImageSerializer,
    PostCreateSerializer
)
from .permissions import (
    IsPostWriter,
)


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_classes = {
        "create": PostCreateSerializer,
    }
    permission_classes = {
        "list": [],
        "retrieve": [],
        "create": [],
        "update": [IsPostWriter],
        "destroy": [IsPostWriter],
    }
    template_names = {
        "list": ['post_list.html'],
        "retrieve": ['post_detail.html'],
    }

    def get_permissions(self):
        return [permission() for permission in self.permission_classes.get(self.action, [])]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class PostImageView(CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer
    lookup_field = "id"

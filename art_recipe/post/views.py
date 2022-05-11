from rest_framework.viewsets import ModelViewSet
from rest_framework import decorators
from .models import Post, Material, PostImage
from .serializers import (
    PostSerializer,
    PostCreateSerializer
)
from .permissions import (
    IsPostWriter,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['writer', 'bookmarkers']
    search_fields = ['title', 'writer__username', 'desc', 'materials__name']

    def get_permissions(self):
        return [permission() for permission in self.permission_classes.get(self.action, [])]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    @decorators.action(detail=True, methods=["POST"])
    def bookmark(self, request, *args, **kwargs):
        post = self.get_object()
        post.bookmark(request.user)
        return self.retrieve(request, *args, **kwargs)

    
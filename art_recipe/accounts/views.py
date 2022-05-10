from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework import mixins
from .models import User, Profile
from .serializers import (
    UserSerializer,
    ProfileSerializer,
)
from accounts.permissions import IsMyProfile

class ProfileViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsMyProfile]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class UserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
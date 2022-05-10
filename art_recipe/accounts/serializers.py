from rest_framework import serializers
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]

    def create(self, validated_data):
        user = self.context["request"].user
        profile = Profile(**validated_data, user=user)
        profile.save()
        return profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "profile",
            "username",
            "last_login",
            "date_joined",
            "email",
        ]
        
    profile = ProfileSerializer()
        
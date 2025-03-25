from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from rest_framework.exceptions import ValidationError


class UserConfirmation(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=30)
    password = serializers.CharField(min_length=3, max_length=6)


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True},
            'email': {'required': True},
        }

    def validate_username(self, value):
        # Проверка, что username не занят
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already in use")
        return value

    def validate_email(self, value):
        # Проверка, что email не занят
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use")
        return value



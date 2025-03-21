from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=100)
    password = serializers.CharField(min_length=6, max_length=100)

class UserAuthSerializer(UserBaseSerializer):
    pass

class UserRegistrationSerializer(UserBaseSerializer):
    pass

    def validate_username(self,username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('Username already exists')



from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import ConfirmationCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =["id","username","password","email","code","is_active"]

class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=100)
    password = serializers.CharField(min_length=6, max_length=100)

class UserConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

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



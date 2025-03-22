from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random
from django.core.mail import send_mail
from . import models
from .models import SMSCode
from .serializers import (UserRegistrationSerializer,
                          UserAuthSerializer,
                          UserConfirmation)


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=serializer.validated_data.get('username'),
        email=serializer.validated_data.get('email'),
        password=serializer.validated_data.get('password'),
        is_active=False
    )

    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    SMSCode.objects.create(code=code, user=user)

    send_mail(
        'Your code',
        message=code,
        from_email='<EMAIL>',
        recipient_list=[user.email]
    )
    return Response({"message": "Код отправлен на email"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def confirmation_api_view(request):
    serializer = UserConfirmation(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    email = serializer.validated_data.get('email')
    code = serializer.validated_data.get('code')
    try:
        confirm_record = models.SMSCode.objects.get(user__email=email, code=code)
    except models.SMSCode.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'message','code not found'})
    confirm_record.user.is_active = True
    confirm_record.user.save()
    confirm_record.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data = {'User credentials are wrong'})
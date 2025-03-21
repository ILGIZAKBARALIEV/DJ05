from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from .models import ConfirmationCode
from .serializers import (UserSerializer,
                          UserAuthSerializer,
                          UserConfirmationCodeSerializer)


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserSerializer (data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    email = serializer.validated_data.get('email')

    if not username or not password or not email:
        return Response ({"error": "требуется имя пользователя, пароль, адрес электронной почты"},status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username,password=password,email=email).exists():
        return Response({"error": "имя пользователя пароль адрес электронной почты был создан"},status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username,password=password,email=email,is_active=False)
    code = get_random_string(length=6,allowed_chars='0123456789')
    ConfirmationCode.objects.create(user=user,code=code)

    send_mail(
        'Your code',
        message=code,
        from_email='<EMAIL>',
        recipient_list=[user.email]
    )
    return Response({"message": "Код отправлен на email"},status=status.HTTP_200_OK)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)

    if user is not None:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response({'key':token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data = {'User credentials are wrong'})

@api_view(['POST'])
def confirmation_api_view(request):
    serializer = UserConfirmationCodeSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('user')
        password = serializer.validated_data.get('password')
        email = serializer.validated_data.get('email')
        code = serializer.validated_data.get('code')
        try:
            username = User.objects.get(username=username, email=email)
            confirmation = ConfirmationCode.objects.get(user=username,password=password, code=code)
        except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
            return Response({"error": "Неверный email или код"},status= status.HTTP_400_BAD_REQUEST)

        username.is_active=True
        username.save()
        confirmation.delete()

        return Response({"message": "Пользователь успешно подтвержден"},status= status.HTTP_200_OK)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




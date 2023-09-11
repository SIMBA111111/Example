from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from users import serializers

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = serializers.RegistrationSerializer


@extend_schema_view(
    post=extend_schema(
        request=serializers.ChangePasswordSerializer,
        summary='Смена пароля', tags=['Аутентификация & Авторизация']),
)
class ChangePasswordView(APIView):

    def post(self, request):
        user = request.user
        serializer = serializers.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)


@extend_schema_view(
    get=extend_schema(summary='Профиль пользователя', tags=['Пользователи']),
    put=extend_schema(summary='Изменить профиль пользователя', tags=['Пользователи']),
    patch=extend_schema(summary='Изменить частично профиль пользователя', tags=['Пользователи']),
)
class MeView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.MeSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return serializers.MeUpdateSerializer
        return serializers.MeSerializer

    def get_object(self):
        return self.request.user
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from author.serializers import AuthorMeSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)


class UserMeSerializer(serializers.ModelSerializer):
    author = AuthorMeSerializer()

    class Meta:
        model = User
        fields = [
            'id', 'last_login', 'username', 'first_name', 'last_name', 'email',
            'is_staff', 'is_active', 'date_joined', 'author'
        ]


class CreateAccountSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    type = serializers.ChoiceField(choices=['author', 'user'])

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'type'
        ]

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserOTP


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True),
    email = serializers.EmailField(max_length=255, min_length=8),
    first_name = serializers.CharField(max_length=255, min_length=2),
    last_name = serializers.CharField(max_length=255, min_length=2),
    #mobile_num = serializers.IntegerField(default=1234567890)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile_num', 'email', 'password', )


    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True),
    username = serializers.CharField(max_length=255, min_length=2),

    class Meta:
        model = User
        fields = ['username', 'password']


class OtpSerializer(serializers.ModelSerializer):
     class Meta:
        model = UserOTP
        fields = ['otp']





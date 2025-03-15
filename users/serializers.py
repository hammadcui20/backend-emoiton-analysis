from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import LoginSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'dob', 'phone_number']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'dob']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            dob=validated_data['dob']
        )
        return user


class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Check if user is a super admin
        data["role"] = "admin" if user.is_admin_user else "user"

        # Include any additional user details if needed
        data["email"] = user.email
        data["username"] = user.username

        return data


# Admin
from rest_framework import serializers


class PerformanceSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    new_users_last_30_days = serializers.IntegerField()

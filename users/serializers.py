from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import LoginSerializer


class UserSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'dob', 'phone_number', 'user_role']

    def get_user_role(self, obj):
        if obj.is_admin_user:
            return "admin"
        elif obj.is_analyst:
            return "user"
        return "user"


from rest_framework.validators import UniqueValidator
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'dob', 'role']

    def get_role(self, obj):
        """Determine the user's role based on their flags."""
        if obj.is_admin_user:
            return "admin"
        elif obj.is_analyst:
            return "user"
        return "user"

    def create(self, validated_data):
        """Create a new user if validation passes."""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),  # Use .get() for optional fields
            dob=validated_data.get('dob')
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
        data["dob"] = user.dob
        data["phone_number"] = user.phone_number

        return data


# Admin
from rest_framework import serializers


class PerformanceSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    new_users_last_30_days = serializers.IntegerField()

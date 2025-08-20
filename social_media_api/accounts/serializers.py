# accounts/serializers.py
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    # Public-facing representation of a user. We expose safe fields only.
    # The followers/following are represented as counts to keep it lightweight.

    followers_count = serializers.IntegerField(source="followers_count", read_only=True)
    following_count = serializers.IntegerField(source="following_count", read_only=True)


class Meta:
    model = User
    fields = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "bio",
        "profile_picture",
        "followers_count",
        "following_count",
    ]
    read_only_fields = ["id", "followers_count", "following_count"]


class RegisterSerializer(serializers.ModelSerializer):
    # Handles user creation with strong password validation.
    # Note: We ask for password explicitly and write it using set_password.

    password = serializers.CharField(write_only=True, style={"input_type": "password"})


class Meta:
    model = User
    fields = ["username", "email", "password", "first_name", "last_name"]


def validate_password(self, value):
    # Leverage Django's built-in password validators (if configured)
    validate_password(value)
    return value


def create(self, validated_data):
    # Use create_user so password is hashed and defaults are applied
    password = validated_data.pop("password")
    user = User.objects.create_user(**validated_data)
    user.set_password(password)
    user.save()
    return user


class ProfileUpdateSerializer(serializers.ModelSerializer):
    # Allows the authenticated user to update their own profile fields.
    # We intentionally exclude username/email changes here to keep it simple.

    class Meta:
        model = User
        fields = ["first_name", "last_name", "bio", "profile_picture"]

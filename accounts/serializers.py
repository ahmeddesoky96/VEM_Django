from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
# from .models import *
# from django.db.models import fields


User=get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields = ('id', 'email', 'first_name', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'email', 'first_name', 'last_name')
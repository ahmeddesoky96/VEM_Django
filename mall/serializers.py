from rest_framework import serializers
from .models import *
from django.db.models import fields

class Shopserializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        

# farm/serializers.py

from rest_framework import serializers
from .models import Farm

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'user', 'location', 'crop_type', 'boundaries', 'area', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

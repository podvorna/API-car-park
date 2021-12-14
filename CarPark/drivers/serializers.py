from re import S
from rest_framework import serializers
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    class Meta:
        model = Driver
        fields = '__all__'

class CreateDriverSerializer(serializers.ModelSerializer):
    first_name = serializers.JSONField()
    last_name = serializers.JSONField()
    
    class Meta:
        model = Driver
        fields = ('first_name', 'last_name')

    


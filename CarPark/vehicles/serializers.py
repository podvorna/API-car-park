from rest_framework import serializers
from .models import Vehicle
from drivers.serializers import DriverSerializer

class VehicleSerializer(serializers.ModelSerializer):
    driver_id = DriverSerializer(many=True)
  
    id = serializers.IntegerField()
    driver_id = serializers.CharField()
    model = serializers.CharField(max_length=150)
    make = serializers.CharField(max_length=150)
    plate_number = serializers.RegexField(regex='/^[А-Я]{2} [0-9]{4} [А-Я]{2}$/')
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
    # driver_id = DriverSerializer(many=True)
     
    class Meta:
        model = Vehicle
        fields = '__all__'
        
        
class CreateVehicleSerializer(serializers.ModelSerializer):
    # driver_id = DriverSerializer(many=False)
    

    model = serializers.JSONField()
    make = serializers.JSONField()
    plate_number = serializers.JSONField()
    
    class Meta:
        model = Vehicle
        fields = ('driver_id', 'model', 'make', 'plate_number')
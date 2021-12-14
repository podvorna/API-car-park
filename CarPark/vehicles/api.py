from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters


from .serializers import VehicleSerializer, CreateVehicleSerializer
from .models import Vehicle
# from CarPark.drivers import serializers

class VehicleListAPIView(ListAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    
    def post(self,request):
            serializer = CreateVehicleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

    
class VehicleDetailAPIView(RetrieveAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = 'id'
   
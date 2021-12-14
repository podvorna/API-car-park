from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters


from .serializers import DriverSerializer,CreateDriverSerializer
from .models import Driver
# from CarPark.drivers import serializers

class DriverListAPIView(ListAPIView):
        serializer_class = DriverSerializer
        queryset = Driver.objects.all()
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['created_at']
        
        def post(self,request):
            serializer = CreateDriverSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)


class DriverDetailAPIView(RetrieveAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    lookup_field = 'id'
    
    # def DriverDelete(request, pk):
    #     driver = Driver.objects.get(id=pk)
    #     driver.delete()
    #     return Response("Driver Deleted Successfully")

 
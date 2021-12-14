from django.urls import path
from .api import VehicleListAPIView, VehicleDetailAPIView

urlpatterns = [
    path('vehicle/', VehicleListAPIView.as_view(), name = 'vehicle_list'),
    path('vehicle/<str:id>/', VehicleDetailAPIView.as_view(), name = 'vehicle_detail'),
    ]
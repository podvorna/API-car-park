# from rest_framework import routers
from django.urls import path
from .api import DriverDetailAPIView, DriverListAPIView, DriverDetailAPIView
# from . import views
# router = routers.DefaultRouter()
# router.register('drivers/', DriverViewSet, 'driver')
# # router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = [
    path('driver/', DriverListAPIView.as_view(), name = 'driver_list'),
    path('driver/<str:id>/', DriverDetailAPIView.as_view(), name = 'driver_detail'),
    
    ]
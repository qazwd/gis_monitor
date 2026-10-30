# from django.shortcuts import render
from rest_framework import viewsets
from .models import Person, Vehicle
from .serializers import PersonSerializer, VehicleSerializer

# Create your views here.
# 人员 API ：支持 GET（查询）、POST（添加）、PUT（修改）、DELETE（删除）
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# 车辆 API ：支持 GET（查询）、POST（添加）、PUT（修改）、DELETE（删除）
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

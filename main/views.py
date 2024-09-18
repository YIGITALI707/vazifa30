from django.shortcuts import render
from  rest_framework.generics import ListAPIView
from .models import Cars
from .serializers import CarsSerializers
# Create your views here.


class CarsAPIView(ListAPIView):
    queryset =Cars.objects.all()
    serializer_class =CarsSerializers

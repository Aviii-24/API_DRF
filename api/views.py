from django.shortcuts import render

from rest_framework import viewsets
from .models import WheelSpecification, BogieChecksheet
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer

class WheelSpecificationViewSet(viewsets.ModelViewSet):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer

class BogieChecksheetViewSet(viewsets.ModelViewSet):
    queryset = BogieChecksheet.objects.all()
    serializer_class = BogieChecksheetSerializer


from rest_framework import serializers
from .models import WheelSpecification, BogieChecksheet  # your models

class WheelSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

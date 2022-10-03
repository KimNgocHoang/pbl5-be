from dataclasses import field
from .models import Plant, History_Pest, History_Water
from rest_framework import serializers

class PlantCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Plant
        fields = [
            'plant_name',
            'alarm',
            'humidity',
            'threadhold',
        ]

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        # It is strongly recommended that you explicitly set all fields that should be serialized using the fields attribute
        fields = '__all__'

class HistoryPestSerializer(serializers.ModelSerializer):
    class Meta:
        model = History_Pest
        fields = '__all__'

class HistoryWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = History_Water
        fields = '__all__'
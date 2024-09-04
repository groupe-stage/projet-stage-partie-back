from rest_framework import serializers
from Surveillance.models import Surveillance

class SurveillanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveillance
        fields = '__all__'

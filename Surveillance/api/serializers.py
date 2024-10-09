from rest_framework import serializers
from Surveillance.models import Surveillance

class SurveillanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveillance
        fields = '__all__'


    def update(self, instance, validated_data):
        # Allow only the 'user_id' field to be updated
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance
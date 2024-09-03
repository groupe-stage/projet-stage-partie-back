from rest_framework import serializers
from Examen.models import Examen
from Session.models import Session
from Module.models import Module

class ExamenSerializer(serializers.ModelSerializer):
    id_session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    id_module = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all())

    class Meta:
        model = Examen
        fields = '__all__'

from rest_framework import serializers
from sallex.models import Sallex
from Salle.models import Salle
from Examen.models import Examen

class SallexSerializer(serializers.ModelSerializer):
    id_salle = serializers.PrimaryKeyRelatedField(queryset=Salle.objects.all())
    id_examen = serializers.PrimaryKeyRelatedField(queryset=Examen.objects.all())
    
    class Meta:
        model = Sallex
        fields = '__all__'

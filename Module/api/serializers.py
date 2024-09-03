from rest_framework import serializers
from Module.models import Module
from Niveau.models import Niveau
class ModuleSerializer(serializers.ModelSerializer):
    id_niveau = serializers.PrimaryKeyRelatedField(queryset=Niveau.objects.all())

    class Meta:
        model = Module
        fields = '__all__'

from rest_framework import serializers
from Contrainte.models import Contrainte
from Users.models import AppUser

class ContrainteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.all())

    class Meta:
        model = Contrainte
        fields = '__all__'

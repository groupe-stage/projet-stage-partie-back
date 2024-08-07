from rest_framework import serializers
from Users.models import Users

class UsersSerializer(serializers.ModelSerializer):
    image_user = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Users
        fields = '__all__'
   

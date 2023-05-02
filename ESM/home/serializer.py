from rest_framework.serializers import ModelSerializer
from .models import TUser

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = TUser
        fields = '__all__'
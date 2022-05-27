from .models import *
from rest_framework import serializers
 

# -------------------------------------------- Provider ------------------------------------------ #
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderModel
        fields = '__all__'

# -------------------------------------------- Service ------------------------------------------ #
class ServiceSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False, read_only=True)

    class Meta:
        model = ServiceModel
        fields = '__all__'

    
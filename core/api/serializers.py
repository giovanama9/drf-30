from rest_framework import serializers
from core.models import Abrigo
from core.models import Animal


class AbrigoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Abrigo
        fields= '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
from rest_framework import serializers
from ..models import Pet

from apps.authentication.api.serializers import UserSerializer


class PetSerializer(serializers.ModelSerializer):
    donatario = serializers.SerializerMethodField()

    def get_donatario(self, obj):
        return UserSerializer(obj.donatario).data

    class Meta:
        model = Pet
        fields = "__all__"
        read_only_fields = ("donatario", "adotante")

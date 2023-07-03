from rest_framework import serializers
from ..models import Pet


class PetSerializer(serializers.ModelSerializer):
    donatario = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = "__all__"
        read_only_fields = ("donatario", "adotante")

from rest_framework import serializers
from ..models import Pet, Picture

from apps.authentication.api.serializers import UserSerializer


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = "__all__"


class PetSerializer(serializers.ModelSerializer):
    donatario = serializers.SerializerMethodField()
    pictures = serializers.SerializerMethodField()

    def get_donatario(self, obj):
        return UserSerializer(obj.donatario).data

    def get_pictures(self, obj):
        # Get pictures and serialize them
        pictures_data = PictureSerializer(obj.pictures.all(), many=True).data

        # Modify the image URL to include the full path
        for picture in pictures_data:
            if self.context.get("request"):
                picture["image"] = self.context["request"].build_absolute_uri(
                    picture["image"]
                )

        return pictures_data

    class Meta:
        model = Pet
        fields = "__all__"
        read_only_fields = ("donatario", "adotante")

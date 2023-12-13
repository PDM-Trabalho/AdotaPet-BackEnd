from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from django.contrib.auth import get_user_model

from ..models import Profile, Address


# TODO: na edição de usuario tem que ter alguns campos que na verdade serao editados do profile
# na deleção de usuario, tem que levar o profile dele junto


# class AddressSerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = Address
#         fields = "__all__"
#         geo_field = "geometry"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    favorite_pets = serializers.SerializerMethodField()

    def get_address(self, obj):
        return AddressSerializer(obj.address).data

    def get_favorite_pets(self, obj):
        from apps.adopt.api.serializers import PetSerializer

        return PetSerializer(obj.favorite_pets, many=True).data

    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)
    profile = serializers.SerializerMethodField()

    def get_profile(self, obj):
        data = ProfileSerializer(obj.profile).data
        if self.context.get("request"):
            data["picture"] = self.context["request"].build_absolute_uri(
                data["picture"]
            )
        return data

    class Meta:
        model = get_user_model()
        exclude = [
            "last_login",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
            "date_joined",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        password_confirmation = validated_data.pop("password_confirmation")

        if password != password_confirmation:
            raise serializers.ValidationError({"error": "passwords didn't match"})

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        return user

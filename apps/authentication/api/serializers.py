from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from django.contrib.auth import get_user_model

from ..models import Profile, Address


# TODO: na edição de usuario tem que ter alguns campos que na verdade serao editados do profile
# na deleção de usuario, tem que levar o profile dele junto


class AddressSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        geo_field = "geometry"


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

from rest_framework import serializers

from django.contrib.auth import get_user_model

from ..models import Profile


# TODO: na edição de usuario tem que ter alguns campos que na verdade serao editados do profile
# na deleção de usuario, tem que levar o profile dele junto


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")
        password_confirmation = validated_data.pop("password_confirmation")

        if password != password_confirmation:
            raise serializers.ValidationError({"error": "passwords didn't match"})

        user = super().create(validated_data)
        Profile.objects.create(user=user)
        return user

from django.db import models
from django.contrib.gis.db import models as gis_models

from django.conf import settings

USER_MODEL_STRING = settings.AUTH_USER_MODEL

from apps.adopt.models import Pet


class Address(models.Model):
    street = gis_models.CharField(max_length=255, blank=True, null=True)
    city = gis_models.CharField(max_length=255, blank=True, null=True)
    state = gis_models.CharField(max_length=255, blank=True, null=True)
    geometry = gis_models.PointField()


class Profile(models.Model):
    user = models.OneToOneField(
        USER_MODEL_STRING, on_delete=models.CASCADE, related_name="profile"
    )
    phone = models.CharField(
        max_length=11, verbose_name="telefone", blank=True, null=True
    )
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, blank=True, null=True
    )
    favorite_pets = models.ManyToManyField(Pet, blank=True)

    def __str__(self) -> str:
        return f"Perfil de: {self.user.username}"
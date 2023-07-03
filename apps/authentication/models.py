from django.db import models

from django.conf import settings

USER_MODEL_STRING = settings.AUTH_USER_MODEL


class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=2)


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

    def __str__(self) -> str:
        return f"Perfil de: {self.user.username}"

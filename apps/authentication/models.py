from django.db import models

from django.conf import settings

USER_MODEL_STRING = settings.AUTH_USER_MODEL


class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=2)
    user = models.ForeignKey(
        USER_MODEL_STRING,
        on_delete=models.CASCADE,
        related_name="addresses",
        related_query_name="address",
    )


class Profile(models.Model):
    user = models.OneToOneField(
        USER_MODEL_STRING, on_delete=models.CASCADE, related_name="profile"
    )
    phone = models.CharField(max_length=11, verbose_name="telefone")

    def __str__(self) -> str:
        return f"Perfil de: {self.user.username}"

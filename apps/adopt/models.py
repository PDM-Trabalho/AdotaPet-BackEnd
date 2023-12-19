from django.db import models
from django.conf import settings

USER_MODEL_STRING = settings.AUTH_USER_MODEL


class Pet(models.Model):
    class Porte(models.TextChoices):
        PEQUENO = "P", "Pequeno"
        MEDIO = "M", "Médio"
        GRANDE = "G", "Grande"

    class Sexo(models.TextChoices):
        MACHO = "M", "Macho"
        FEMEA = "F", "Fêmea"

    especie = models.CharField(max_length=50)

    raça = models.CharField(max_length=50)

    porte = models.CharField(max_length=1, choices=Porte.choices, default=Porte.PEQUENO)

    sexo = models.CharField(max_length=1, choices=Sexo.choices)

    idade = models.IntegerField()

    altura = models.IntegerField()

    comprimento = models.IntegerField()

    donatario = models.ForeignKey(
        USER_MODEL_STRING,
        on_delete=models.CASCADE,
        related_name="donated_pets",
        blank=True,
        null=True,
    )

    adotante = models.ForeignKey(
        USER_MODEL_STRING,
        on_delete=models.CASCADE,
        related_name="adopted_pets",
        blank=True,
        null=True,
    )


class Picture(models.Model):
    image = models.ImageField(upload_to="pics", null=True, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="pictures")

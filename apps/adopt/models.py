from django.db import models

from django.conf import settings

USER_MODEL_STRING = settings.AUTH_USER_MODEL


class Pet(models.Model):
    class EscolhasDePorte(models.TextChoices):
        PEQUENO = "P", "Pequeno"
        MEDIO = "M", "Médio"
        GRANDE = "G", "Grande"

    class EscolhasDeSexo(models.TextChoices):
        MACHO = "M", "Macho"
        FEMEA = "F", "Fêmea"

    especie = models.CharField(max_length=50)
    raça = models.CharField(max_length=50)
    porte = models.CharField(
        max_length=1, choices=EscolhasDePorte, default=EscolhasDePorte.PEQUENO
    )
    sexo = models.CharField(max_length=1, choices=EscolhasDeSexo)
    idade = models.IntegerField()
    # foto=
    altura = models.DecimalField()
    comprimento = models.DecimalField()
    peso = models.DecimalField()
    donatario = models.ForeignKey(USER_MODEL_STRING, on_delete=models.CASCADE)
    adotante = models.ForeignKey(USER_MODEL_STRING, on_delete=models.CASCADE)

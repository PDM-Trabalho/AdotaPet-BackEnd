# Generated by Django 4.2.2 on 2023-07-03 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("especie", models.CharField(max_length=50)),
                ("raça", models.CharField(max_length=50)),
                (
                    "porte",
                    models.CharField(
                        choices=[("P", "Pequeno"), ("M", "Médio"), ("G", "Grande")],
                        default="P",
                        max_length=1,
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Macho"), ("F", "Fêmea")], max_length=1
                    ),
                ),
                ("idade", models.IntegerField()),
                ("altura", models.DecimalField(decimal_places=2, max_digits=3)),
                ("comprimento", models.IntegerField()),
                ("peso", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "adotante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="adopted_pets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "donatario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donated_pets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

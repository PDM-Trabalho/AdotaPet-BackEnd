# Generated by Django 4.2.8 on 2023-12-11 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("adopt", "0002_alter_pet_foto"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="foto",
        ),
        migrations.CreateModel(
            name="Picture",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="pics")),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="adopt.pet"
                    ),
                ),
            ],
        ),
    ]

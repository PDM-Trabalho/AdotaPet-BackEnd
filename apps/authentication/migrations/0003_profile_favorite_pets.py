# Generated by Django 4.2.2 on 2023-07-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adopt", "0002_alter_pet_adotante_alter_pet_donatario"),
        ("authentication", "0002_remove_address_user_profile_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="favorite_pets",
            field=models.ManyToManyField(to="adopt.pet"),
        ),
    ]

# Generated by Django 4.2.2 on 2024-02-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True,
                default="last name",
                max_length=255,
                null=True,
                verbose_name="Apellidos",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                blank=True,
                default="name",
                max_length=255,
                null=True,
                verbose_name="Nombres",
            ),
        ),
    ]

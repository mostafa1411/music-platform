# Generated by Django 4.1.2 on 2022-10-24 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0007_album_created_album_modified"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("name", models.CharField(default="", max_length=50)),
                ("image", models.ImageField(upload_to="images/%y/%m/%d")),
                ("audio", models.FileField(upload_to="audio/%y/%m/%d")),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="albums.album"
                    ),
                ),
            ],
        ),
    ]

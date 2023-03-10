# Generated by Django 4.1.5 on 2023-02-04 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("animal_views", models.IntegerField(default=0)),
                ("animal_likes", models.IntegerField(default=1)),
                ("animal_name", models.CharField(max_length=100)),
                ("animal_description", models.TextField()),
                ("animal_slug", models.SlugField(max_length=1000, unique=True)),
                (
                    "animal_gender",
                    models.CharField(
                        choices=[("MALE", "MALE"), ("FEMALE", "FEMALE")], max_length=100
                    ),
                ),
            ],
            options={
                "ordering": ["animal_name"],
            },
        ),
        migrations.CreateModel(
            name="AnimalBreed",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("animal_breed", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AnimalColor",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("animal_color", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("category_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AnimalLocation",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("loaction", models.CharField(max_length=100)),
                (
                    "animals",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="location",
                        to="home.animal",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AnimalImages",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now_add=True)),
                ("animal_images", models.ImageField(upload_to="animals")),
                (
                    "animals",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="home.animal",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="animal",
            name="animal_breed",
            field=models.ManyToManyField(null=True, to="home.animalbreed"),
        ),
        migrations.AddField(
            model_name="animal",
            name="animal_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="animal_category",
                to="home.category",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="animal_color",
            field=models.ManyToManyField(null=True, to="home.animalcolor"),
        ),
        migrations.AddField(
            model_name="animal",
            name="animal_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="animals",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

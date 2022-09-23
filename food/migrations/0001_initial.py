# Generated by Django 4.1.1 on 2022-09-23 15:47

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
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Drinks and Beverages", "Drinks and Beverages"),
                            ("Meat", "Meat"),
                            ("Side Dish", "Side Dish"),
                            ("Snacks", "Snacks"),
                            ("Chicken", "Chicken"),
                            ("other", "other"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                (
                    "order_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("date_order", models.DateTimeField(auto_now_add=True)),
                ("order_started", models.BooleanField(default=False)),
                ("delivered", models.BooleanField(default=False)),
                (
                    "order_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Food",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.FloatField()),
                ("availability", models.BooleanField(default=True)),
                ("image", models.ImageField(upload_to="")),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="food.category",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_remove_customuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="delivery_address",
            field=models.TextField(default=""),
        ),
    ]
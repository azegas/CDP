# Generated by Django 4.2.6 on 2023-10-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]

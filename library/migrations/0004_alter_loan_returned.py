# Generated by Django 5.1.3 on 2024-11-25 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_loan_returned"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="returned",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
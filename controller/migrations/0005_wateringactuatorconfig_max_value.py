# Generated by Django 4.2.16 on 2024-11-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0004_wateringactuatorconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='wateringactuatorconfig',
            name='max_value',
            field=models.FloatField(default=20),
            preserve_default=False,
        ),
    ]

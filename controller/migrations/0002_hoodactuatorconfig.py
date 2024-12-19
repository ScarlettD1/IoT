# Generated by Django 4.2.16 on 2024-10-13 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoodActuatorConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_value', models.FloatField()),
                ('fan_speed', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-10-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_rename_solar_type_weather_soil_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='city',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

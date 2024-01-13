# Generated by Django 4.2.2 on 2023-06-17 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiciant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_performance',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='tools',
            field=models.CharField(choices=[('drums', 'баробаны'), ('violin', 'скрипка'), ('flute', 'флейта'), ('guitarac', 'гитара')], max_length=30),
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='custattendance',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='custattendance',
            name='Workout',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

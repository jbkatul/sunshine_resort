# Generated by Django 4.1.5 on 2023-01-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='days',
            field=models.IntegerField(),
        ),
    ]

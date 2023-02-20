# Generated by Django 4.1.5 on 2023-01-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('days', models.IntegerField(max_length=100)),
                ('adhar_no', models.CharField(max_length=100)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('no_of_persons', models.IntegerField(max_length=100)),
                ('room_type', models.CharField(choices=[('SR', 'Standard'), ('DR', 'Deluxe'), ('SD', 'Super Deluxe'), ('TR', 'Tent')], max_length=2)),
            ],
        ),
    ]

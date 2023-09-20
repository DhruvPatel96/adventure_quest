# Generated by Django 4.1.7 on 2023-03-27 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_reservation_booking_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height_limit', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('duration', models.DurationField()),
            ],
        ),
    ]
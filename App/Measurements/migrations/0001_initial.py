# Generated by Django 4.2 on 2023-04-12 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Humidity', models.CharField(max_length=20)),
                ('CarbonDioxide', models.CharField(max_length=20)),
                ('Oxygen', models.CharField(max_length=20)),
                ('Temperature', models.CharField(max_length=20)),
                ('Pressure', models.CharField(max_length=20)),
                ('Power', models.CharField(max_length=20)),
                ('registration_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
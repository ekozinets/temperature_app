# Generated by Django 4.1.1 on 2022-10-05 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'cities',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CityTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date measured')),
                ('temperature_value', models.IntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature.city')),
            ],
            options={
                'db_table': 'city_temperatures',
                'ordering': ['date'],
            },
        ),
    ]